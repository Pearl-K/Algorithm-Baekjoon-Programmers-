#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;

int N, M, T;
int grid[101][101];
bool vst[101][101][2] = {false, };
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

bool checkRange(int r, int c) {
	return (0<=r && r<N && 0<=c && c<M);
}

int bfs() {
	// {time, r, c, sword}
	queue<vi> q;
	q.push({0, 0, 0, 0});

	while(!q.empty()) {
		vi now = q.front();
		q.pop();
		int time = now[0];
		int r = now[1];
		int c = now[2];
		int sword = now[3];

		if (time > T) continue;
		if (r == N-1 && c == M-1) return time;

		for(int d=0; d<4; ++d){
			int nr = r + dr[d];
			int nc = c + dc[d];

			if(checkRange(nr, nc)){
				if(sword == 1 && !vst[nr][nc][1]){
					vst[nr][nc][1] = true;
					q.push({time+1, nr, nc, sword});
				}
				else if(!vst[nr][nc][0] && grid[nr][nc] == 2){
					vst[nr][nc][0] = true;
					q.push({time+1, nr, nc, 1});
				}
				else {
					if(!vst[nr][nc][0] && grid[nr][nc] == 0){
						vst[nr][nc][0] = true;
						q.push({time+1, nr, nc, sword});
					}
				}
			}
		}
	}
	return -1;
}

int main(){
	cin.tie(0)->sync_with_stdio(0);
	cin >> N >> M >> T;
	for(int i=0; i<N; ++i){
		for(int j=0; j<M; ++j){
			cin >> grid[i][j];
		}
	}
	int ret = bfs();
	if (ret == -1) cout << "Fail" << "\n";
	else cout << ret << "\n";
	return 0;
}
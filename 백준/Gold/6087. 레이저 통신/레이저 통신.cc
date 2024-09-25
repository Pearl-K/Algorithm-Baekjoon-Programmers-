#include <bits/stdc++.h>
using namespace std;
using pi = pair<int, int>;

int W, H;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

char grid[101][101];
int check[101][101][4];
int raser[101][101][4];
pi start, finish;

void bfs(pi pos){
	queue<pair<pi, int>> Q; //위치, 방향 순서로 저장
	Q.push({pos, -1}); // -1으로 방향 없는 상태 초기화

	for(int i = 0; i < 4; i++){
		check[pos.first][pos.second][i] = 1;
		raser[pos.first][pos.second][i] = 0;
	}

	while(!Q.empty()){
		int x = Q.front().first.first;
		int y = Q.front().first.second;
		int d = Q.front().second;
        Q.pop();

		for(int i = 0; i < 4; i++){
			int nx = x + dx[i];
			int ny = y + dy[i];

			if(nx >= 1 && nx <= H && ny >= 1 && ny <= W){
				if(grid[nx][ny] == '*') continue;

				if(d == i){
					if(check[nx][ny][i] == 0){
						raser[nx][ny][i] = raser[x][y][d];
						check[nx][ny][i] = 1;
						Q.push({{nx,ny}, i});
					} else {
						if(raser[nx][ny][i] > raser[x][y][d]){
							raser[nx][ny][i] = raser[x][y][d];
							Q.push({{nx, ny},i});
						}
					}
				} else{
					if(check[nx][ny][i] == 0){
						raser[nx][ny][i] = raser[x][y][d] + 1;
						check[nx][ny][i] = 1;
						Q.push({{nx,ny}, i});
					} else {
						if(raser[nx][ny][i] > raser[x][y][d] + 1){
							raser[nx][ny][i] = raser[x][y][d] + 1;
							Q.push({{nx,ny},i});
						}
					}
				}	
			}
		}
	}
}

int main() {
	cin.tie(0);
	cout.tie(0);
    ios::sync_with_stdio(0);

	cin >> W >> H;
	for(int i= 1; i <= H; i++){
		for(int j = 1; j <= W; j++){
			cin >> grid[i][j];

			if(grid[i][j] == 'C' && start.first == 0) start = {i,j};
			else if(grid[i][j] == 'C') finish = {i,j};
		}
	}
    int MIN = 100000001;
    bfs(start);

    for(int i = 0; i < 4; i++){
        if(check[finish.first][finish.second][i] == 0) continue;
        MIN = min(MIN, raser[finish.first][finish.second][i]);
    }
    cout << MIN-1 << "\n";
	return 0;
}

#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int ret;
int sr, sc;
int map[20][20];
int dir[4][2] = { {1,1},{1,-1},{-1,-1},{-1,1} };
vector<int> path;

void dfs(int r, int c, int d) {
    int nr = r + dir[d][0];
    int nc = c + dir[d][1];

    if (d == 3 && nr == sr && nc == sc) {
        int len = path.size();
        if (ret < len) ret = len;
        return;
    }
    if (nr < 0 || nc < 0 || nr >= N || nc >= N) return;
    if (find(path.begin(), path.end(), map[nr][nc]) != path.end()) return;
    path.push_back(map[nr][nc]);

    if (d == 3) {
        dfs(nr, nc, d);
    }
    else {
        dfs(nr, nc, d);
        dfs(nr, nc, d+1);
    }
    path.pop_back();
    return;
}

int main(void){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cin >> N;
        memset(map, 0, sizeof(map));
        for (int i = 0; i < N; i++)  {
            for (int j = 0; j < N; j++)  {
                cin >> map[i][j];
            }
        }

        ret = -1;
        for (int i = 0; i < N-2; i++) {
            for (int j = 1; j < N-1; j++) {
                path.clear();
                path.push_back(map[i][j]);
                sr = i, sc = j;
                dfs(i, j, 0);
            }
        }
        cout << "#" << t << " " << ret << "\n";
    }
    return 0;
}
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int R, C, ret = 0;
int dy[3] = {-1, 0, 1};
vector<vector<bool>> vst;
vector<vector<int>> map;
bool flg = false;

void dfs(int r, int c) {
    if (c == C-1) {
        ret++;
        flg = true;
        return;
    }

    for (int i = 0; i < 3; i++) {
        int nr = r + dy[i];
        int nc = c + 1;

        if (nr >= 0 && nr < R && !vst[nr][nc] && map[nr][nc] == 0) {
            vst[nr][nc] = true;
            dfs(nr, nc);
            if (flg) return;
        }
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> R >> C;
    map.assign(R, vector<int>(C));
    vst.assign(R, vector<bool>(C, false));
    
    for (int i = 0; i < R; ++i) {
        string row;
        cin >> row;
        for (int j = 0; j < C; ++j) {
            map[i][j] = (row[j] == '.') ? 0 : 1;
        }
    }
    
    for (int i = 0; i < R; ++i) {
        flg = false;
        vst[i][0] = true;
        dfs(i, 0);
    }
    cout << ret << '\n';
    return 0;
}
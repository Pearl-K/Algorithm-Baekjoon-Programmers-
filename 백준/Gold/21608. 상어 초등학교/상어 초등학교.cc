#include <iostream>
#include <cstring>
using namespace std;
using pii = pair<int, int>;
const int DIR = 4;
const int MAX = 20*20+1;
const int dr[4] = {-1, 1, 0, 0};
const int dc[4] = {0, 0, -1, 1};
int N;
int totalScore = 0;
int loves[MAX][4];
int grid[21][21];
int maxLove, maxEmpty;
pii bestPos;

bool checkRange(int r, int c){
    return (0 <= r && r < N && 0 <= c && c < N);
}

void updateBestPosition(int me, int r, int c) {
    int loveCnt = 0, emptyCnt = 0;

    for (int i = 0; i < DIR; ++i) {
        int nr = r + dr[i];
        int nc = c + dc[i];

        if (checkRange(nr, nc)) {
            if (grid[nr][nc] == 0) emptyCnt++;
            else {
                for (int j = 0; j < 4; ++j) {
                    if (grid[nr][nc] == loves[me][j]) {
                        loveCnt++;
                        break;
                    }
                }
            }
        }
    }
    
    if (loveCnt > maxLove || (loveCnt == maxLove && emptyCnt > maxEmpty)) {
        maxLove = loveCnt;
        maxEmpty = emptyCnt;
        bestPos = {r, c};
    }
}

void checkScore() {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (grid[i][j] == 0) continue; // 빈칸 제외

            int cntLove = 0;
            for (int d = 0; d < DIR; ++d) {
                int nr = i + dr[d];
                int nc = j + dc[d];

                if (checkRange(nr, nc)) {
                    for (int l = 0; l < 4; ++l) {
                        if (grid[nr][nc] == loves[grid[i][j]][l]) {
                            cntLove++;
                            break;
                        }
                    }
                }
            }
            if (cntLove == 4) totalScore += 1000;
            else if (cntLove == 3) totalScore += 100;
            else if (cntLove == 2) totalScore += 10;
            else if (cntLove == 1) totalScore += 1;
        }
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N;
    memset(grid, 0, sizeof(grid));

    for (int i = 0; i < N * N; ++i) {
        int me;
        cin >> me;
        for (int j = 0; j < 4; ++j) cin >> loves[me][j];
        maxLove = -1, maxEmpty = -1;
        bestPos = {-1, -1};

        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                if (grid[r][c] == 0) {
                    updateBestPosition(me, r, c);
                }
            }
        }
        grid[bestPos.first][bestPos.second] = me;
    }
    checkScore();
    cout << totalScore << "\n";
    return 0;
}
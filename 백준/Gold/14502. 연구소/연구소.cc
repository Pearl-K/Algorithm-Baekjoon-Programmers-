#include <iostream>
#include <queue>
using namespace std;
int N, M;
int ret = 0;
int grid[8][8];
int tmp[8][8];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void copyGrid(int grid[8][8], int tmp[8][8]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            tmp[i][j] = grid[i][j];
        }
    }
}

int virus() {
    int virusGrid[8][8];
    int safeCnt= 0;
    copyGrid(tmp, virusGrid);
    queue<pair<int, int>> Q;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (virusGrid[i][j] == 2) Q.push(make_pair(i, j));
        }
    }

    while (!Q.empty()) {
        int x = Q.front().first;
        int y = Q.front().second;
        Q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            if (virusGrid[nx][ny] == 0) {
                virusGrid[nx][ny] = 2;
                Q.push(make_pair(nx, ny));
            }
        }
    }

    for(int i=0; i < N; i++){
        for(int j=0; j < M; j++){
            if(virusGrid[i][j] == 0) safeCnt++;
        }
    }
    return safeCnt;
}

void makeWall(int wallNum) { //wallNum = wall의 개수
    if (wallNum == 3) {
        //벽이 3개일 때 virus 퍼트리고 안전영역 계산
        int safeCnt = virus();
        ret = max(ret, safeCnt);
        return;
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (tmp[i][j] == 0) {
                tmp[i][j] = 1;
                makeWall(wallNum + 1);
                tmp[i][j] = 0;
            }
        }
    }
}

int main(void) {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);

    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> grid[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if(grid[i][j] == 0){
                copyGrid(grid, tmp);
                tmp[i][j] = 1;
                makeWall(1);
                tmp[i][j] = 0;
            }
        }
    }

    cout << ret;
    return 0;
}
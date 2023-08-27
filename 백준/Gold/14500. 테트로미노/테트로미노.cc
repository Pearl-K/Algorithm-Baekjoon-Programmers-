#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int grid[501][501];
int visited[501][501];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int N, M, ret;

void dfs(int x, int y, int cnt, int point){
    if (cnt ==4){
        if(ret < point) ret = point;
        return;
    }

    for(int i=0; i < 4; i++){
        int nx, ny;
        nx = x + dx[i];
        ny = y + dy[i];

        if(nx < 1 || ny < 1 || nx > N || ny > M || visited[nx][ny]) continue;
        visited[nx][ny] = 1;
        dfs(nx, ny, cnt+1, point + grid[nx][ny]);
        visited[nx][ny] = 0;
    }

    //+추가 ㅗ 모양 회전 시킨 상태의 point 계산
    if(x-1 >= 1 && y-1 >= 1 && x+1 <= N) {
        ret = max(ret, (grid[x-1][y] + grid[x][y-1] + grid[x][y] + grid[x+1][y]));
    }
    if(x-1 >= 1 && y+1 <= M && x+1 <= N) {
        ret = max(ret, (grid[x-1][y] + grid[x][y+1] + grid[x][y] + grid[x+1][y]));
    }
    if(y-1 >= 1 && y+1 <= M && x+1 <= N) {
        ret = max(ret, (grid[x][y] + grid[x+1][y] + grid[x+1][y-1] + grid[x+1][y+1]));
    }
    if(y-1 >= 1 && y+1 <= M && x+1 <= N) {
        ret = max(ret, (grid[x][y-1] + grid[x][y] + grid[x][y+1] + grid[x+1][y]));
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    memset(visited, 0, sizeof(visited));

    for(int i=1; i <= N; i++){
        for(int j=1; j <= M; j++){
            cin >> grid[i][j];
        }
    }

    for(int i=1; i <= N; i++){
        for(int j=1; j <= M; j++){
            visited[i][j] = 1;
            dfs(i, j, 1, grid[i][j]);
            visited[i][j] = 0;
        }
    }
    cout << ret;
    return 0;
}
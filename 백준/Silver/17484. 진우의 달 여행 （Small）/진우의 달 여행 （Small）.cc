#include <iostream>
#include <cstring>
using namespace std;
const int INF = 1e9;
int N, M;
int arr[10][10];
int dp[10][10][4];

int dfs(int r, int c, int prevDir){
    if(r == N) return 0;
    int &ret = dp[r][c][prevDir];
    if(ret != INF) return ret;
    if(prevDir != 1) ret = min(ret, dfs(r+1, c, 1)+arr[r][c]);
    if(c-1 >= 0 && prevDir != 0) ret = min(ret, dfs(r+1, c-1, 0)+arr[r][c]);
    if(c+1 < M && prevDir != 2) ret = min(ret, dfs(r+1, c+1, 2)+arr[r][c]);
    return ret;
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    // dp 초기화
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 10; j++)
            for (int k = 0; k < 4; k++)
                dp[i][j][k] = INF;

    cin >> N >> M;
    for(int i=0; i<N; ++i) for(int j=0; j<M; ++j) cin >> arr[i][j];
    int ret = INF;
    for(int i=0; i<M; ++i) ret = min(ret, dfs(0, i, 3));
    cout << ret;
    return 0;
}
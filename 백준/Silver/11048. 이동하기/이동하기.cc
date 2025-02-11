#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int N, M;
int grid[1001][1001];
int dp[1001][1001];

bool checkRange(int r, int c){
    return (0 <= r && r < N && 0 <= c && c < M);
}

int sol(int r, int c){
    if(!checkRange(r, c)) return 0;
    int& ret = dp[r][c];
    if (ret != -1) return ret;
    ret = grid[r][c] + max({sol(r-1, c), sol(r, c-1), sol(r-1, c-1)});
    return ret;
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M;
    memset(dp, -1, sizeof(dp));
    for(int i=0; i<N; ++i) for(int j=0; j<M; ++j) cin >> grid[i][j];
    cout << sol(N-1,M-1);
}
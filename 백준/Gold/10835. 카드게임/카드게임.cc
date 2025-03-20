#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int arr[2][2001];
int dp[2001][2001]; // 현재 카드 인덱스
int N;

int fillDp(int a, int b) {
    if (a >= N || b >= N) return 0;

    int &ret = dp[a][b];
    if (ret != -1) return ret;

    ret = fillDp(a+1, b); // 왼쪽 버림
    ret = max(ret, fillDp(a+1, b+1)); // 둘다 버림
    if (arr[0][a] > arr[1][b]) ret = max(ret, fillDp(a, b+1) + arr[1][b]); //점수 획득
    return ret;
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N;
    for(int i=0; i<N; ++i) cin >> arr[0][i];
    for(int i=0; i<N; ++i) cin >> arr[1][i];
    memset(dp, -1, sizeof(dp));
    cout << fillDp(0, 0) << "\n";
    return 0;
}
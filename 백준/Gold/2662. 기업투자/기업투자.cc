#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
// dp 배낭 문제를 통한 최대 이익금 계산
// N 300(투자 금액), M 20(기업 개수)
// 1원일때 최대, 2원일때 최대, 3원일 때 최대 ...
// n원일 때 최대 구하기 = n원일 때 현재 이득과, 아래 조합에서 합이 n이 되는 것들 중에 최대
// 1 + (N-1), 2 + (N-2), 3+(N-3) 이런식으로 조합해서 여기서 max를 구하는건가?
// 문제는 마지막에 출력할 때 최대 이익을 출력하면서 값 pathTracking이 들어가야 한다

int N, M;
int arr[21][301];
int dp[21][301];
int choice[21][301];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M;
    memset(dp, 0, sizeof(dp));
    int num;
    for(int i=0; i<N; ++i){
        cin >> num;
        for(int j=1; j<=M; ++j) cin >> arr[j][num];
    }
    
    for(int i=1; i<=M; ++i) {
        for(int j=0; j<=N; ++j) {
            dp[i][j] = dp[i-1][j];
            choice[i][j] = 0;
            for(int invest = 1; invest <= j; ++invest) {
                int candidate = dp[i-1][j-invest] + arr[i][invest];
                if (candidate > dp[i][j]) {
                    dp[i][j] = candidate;
                    choice[i][j] = invest;
                }
            }
        }
    }

    cout << dp[M][N] << "\n";
    vector<int> ret(M+1, 0); // pathTracking
    int remain = N;
    for(int i=M; i>=1; --i){
        ret[i] = choice[i][remain];
        remain -= ret[i];
    }
    for(int i=1; i<=M; ++i) cout << ret[i] << " ";
    cout << "\n";
    return 0;
}
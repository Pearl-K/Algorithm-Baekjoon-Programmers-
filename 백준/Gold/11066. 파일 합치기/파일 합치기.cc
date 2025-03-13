#include <iostream>
#include <algorithm>
using namespace std;
const int MAX = 1e9;
int T;
int dp[501][501];
int preSum[501];

void init() {
    for(int i=0; i<501; ++i) preSum[i] = 0;
    for(int i=0; i<501; ++i) for(int j=0; j<501; ++j) dp[i][j] = MAX;
    for(int i = 1; i < 501; ++i) dp[i][i] = 0;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> T;
    
    for(int t=0; t<T; ++t){
        int K;
        cin >> K;
        init();
        
        for(int k=1; k<=K; ++k){
            int tmp;
            cin >> tmp;
            preSum[k] = preSum[k-1]+tmp;
        }
        
        for (int len = 2; len <= K; ++len) {
          for (int i = 1; i <= K - len + 1; ++i) {
              int j = i + len - 1;
              for (int k = i; k < j; ++k) {
                  dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + (preSum[j] - preSum[i-1]));
              }
          }
      }
      cout << dp[1][K] << "\n";
    }
    return 0;
}
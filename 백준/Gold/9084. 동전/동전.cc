#include <iostream>
#include <vector>
using namespace std;
int T, N, K;
int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> T;
    for(int t=0; t < T; t++){
        cin >> N;
        vector<int> c(N+1); //coin

        for(int i=1; i <=N; i++){
            cin >> c[i];
        }

        cin >> K;
        vector<int> dp(K+1);
        dp[0] = 1; //초기화

        for(int i=1; i <= N; i++){
            for(int j=c[i]; j <= K; j++){
                dp[j] += dp[j-c[i]];
            }
        }
        cout << dp[K] << "\n";
    }
    return 0;
}
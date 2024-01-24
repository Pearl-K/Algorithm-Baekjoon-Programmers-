#include <iostream>
using namespace std;
int dp [1500051];
int n;

int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i=1; i <= n; i++){
        int t, p;
        cin >> t >> p;
        dp[i+t] = max(dp[i+t], dp[i]+p);
        dp[i+1] = max(dp[i], dp[i+1]);
    }
    cout << dp[n+1];
    return 0;
}
#include <iostream>
using namespace std;
const int MOD = 1e6;
string code;
int dp[5001] = {0, };

int findCases() {
    int len = code.size();
    if(code[0]=='0') return 0;  // edge case
    dp[0]=1;
    dp[1]=1;

    for(int i=2; i<=len; ++i){
        if(code[i-1] != '0') dp[i]=dp[i-1]%MOD;

        int twoDgit = 10*(code[i-2]-'0') + (code[i-1]-'0');
        if(twoDgit <= 26 && twoDgit >= 10){
            dp[i]=(dp[i]+dp[i-2])%MOD;
        }
    }
    return dp[len];
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> code;
    cout << findCases() << "\n";
    return 0;
}
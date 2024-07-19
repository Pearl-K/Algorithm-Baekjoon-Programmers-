#include <iostream>
#include <vector>

using namespace std;

int N;
const int MOD = 7; //presum%MOD 의 값이 4라면 금요일이다.
int arr[1001];
int cnt[7] = {0, }; // 0~6 까지 개수 카운트
vector<int> dp(7, 0);

int main(void) {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);

    cin >> N;
    for (int n = 0; n < N; n++) {
        cin >> arr[n];
        arr[n] %= MOD;
        cnt[arr[n]]++;
    }

    dp[0] = 1;
    for(int a : arr){
        vector<int> tmp(7, 0);
        for(int i=0; i < 7; i++){
            if(dp[i]){
                tmp[(a+i)%MOD] = 1;
                tmp[i] = 1;
            }
        }
        dp = tmp;
    }

    // 금요일이 되는 조건
    // 1. arr 하나의 값이 4일 때 무조건 금요일 가능
    // 2. arr 일부의 (pre_sum)%MOD = 4 라면 무조건 금요일 가능
    // arr 모든 값에 %MOD 해놓고 그 안에서 dp 생각하면 될듯?

    if (cnt[4] != 0) cout << "YES";
    else if (dp[4]) cout << "YES";
    else cout << "NO";
    return 0;
}
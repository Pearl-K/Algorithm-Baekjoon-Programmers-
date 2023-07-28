#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll m = 1e9+7;

ll pow(ll n){
    if (n ==0) return 1;
    if (n%2 == 1) return (pow(n-1)*2)%m;
    ll H = pow(n/2);
    return (H*H)%m;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;

    ll C, K, ret;
    ret = 0;

    for (int i=0; i < N; i++){
        cin >> C >> K;
        ret = (ret + ((C*K)%m)*pow(K-1))%m;
    }
    cout << ret;
    return 0;
}
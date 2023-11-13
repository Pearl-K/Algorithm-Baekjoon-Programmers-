#include <iostream>
#include <map>
#define MOD 1000000007
using namespace std;
using ll = long long;

ll N;
map<ll, ll> M;

//피보나치 점화식 정리 후 홀짝별로 나타나는 패턴 -> 나눠서 계산
ll fibo(ll x){
    if(M[x]) return M[x];
    ll ret;
    
    if(x % 2 == 0){
        ret = (fibo(x/2)*(fibo(x/2+1)+fibo(x/2-1)))%MOD;
    } else {
        ret = ((fibo((x+1)/2) * fibo((x+1)/2))%MOD)+((fibo((x-1)/2)*fibo((x-1)/2))%MOD)%MOD;
    }
    return M[x] = ret % MOD;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    M[0] = 0;
    M[1] = 1;
    M[2] = 1;
    cout << fibo(N) << "\n";
}
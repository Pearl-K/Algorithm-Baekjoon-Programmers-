#include <iostream>
using namespace std;
using ull = unsigned long long;

int T;
ull S, A, B, K;

// 분할 정복을 통한 빠른 곱 계산 
ull calPow(ull N) {
    // 기저 조건
    if(N == 0) return 1;
    if(N == 1) return 2;
    
    ull ret = calPow(N/2);
    ret = (ret*ret) % S;
    if(N%2 == 1) ret = (2 * ret) % S;
    
    return ret;
}

int main(){
    cin.tie(0)->sync_with_stdio(false);
    cin>>T;
    for(int tc=1; tc <= T; ++tc){
        cin>> A>> B>> K;
        S = A + B; //합을 이용해서 x, y 계산에 이용하면 일반항을 찾을 수 있다.
        
        ull x = (A * calPow(K)) % S;
        ull y = S - x;
        ull ret = min(x, y);
        cout << "#" << tc << " " << ret <<"\n";
    }
    return 0;
}
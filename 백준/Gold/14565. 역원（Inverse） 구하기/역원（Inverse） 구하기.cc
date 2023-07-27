#include <iostream>
using namespace std;
using ll = long long;

ll GCD (ll a, ll c){
    while (c > 0){
        ll temp = a;
        a = c;
        c = temp % c;
    }
    return a;
}

ll extend_gcd(ll a, ll c, ll& x, ll& y){

    if (!c){
        x = 1, y =0;
        return a;
    }

    ll ret = extend_gcd(c, a%c, x, y);
    ll temp = y;
    y = x - (a/c)*y;
    x = temp;

    if (x <= 0){
        x += c;
        y -= a;
    }
    return ret;
}

int main(){
    ll N, A, X, Y;
    cin >> N >> A;

    ll B; //덧셈역 B 구하기
    B = N-A;

    ll ret;
    ret = GCD(N, A);
    if (ret != 1){
        cout << B << " " << -1;
    } else {
        extend_gcd(A, N, X, Y);
        cout << B << " " << X;
    }
    return 0;
}
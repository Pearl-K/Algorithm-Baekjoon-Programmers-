#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using ll = long long;

int GCD(int a, int b){
    int temp;
    while(b != 0){
        temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int A, B;
    cin >> A >> B;

    int ret;
    if (A >= B){
        ret = GCD(A, B);
    } else {
        ret = GCD(B, A);
    }

    ll LCM;
    LCM = (A*B)/ret;
    cout << ret << "\n" << LCM;

    return 0;
}
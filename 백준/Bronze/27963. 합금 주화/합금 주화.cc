#include <iostream>
using namespace std;

int main(void){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);
    
    double d1, d2, x, ret;
    cin >> d1 >> d2 >> x;

    if (d1 > d2) swap(d1, d2);
    double left = (double)(100-x)/x;
    ret = (left+1)/(left*d2/d1+1) *d2;

    cout.precision(6);
    cout << fixed << ret;

}
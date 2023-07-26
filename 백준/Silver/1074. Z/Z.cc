#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int N, R, C, ret;
    ret = 0;

    cin >> N >> R >> C;
    int init_r = pow(2, N)/2;
    int init_c = init_r;

    while (N-- > 0){
        int temp = pow(2, N)/2;
        int sum_v = pow(4, N);

        if (R < init_r && C < init_c){
            init_r -= temp;
            init_c -= temp;
        }
        else if (R < init_r && C >= init_c){
            ret += sum_v;
            init_r -= temp;
            init_c += temp;
        }
        else if (R >= init_r && C < init_c){
            ret += 2*sum_v;
            init_r += temp;
            init_c -= temp;
        }
        else{
            ret += 3*sum_v;
            init_r += temp;
            init_c += temp;
        }
    }
    cout << ret;
}

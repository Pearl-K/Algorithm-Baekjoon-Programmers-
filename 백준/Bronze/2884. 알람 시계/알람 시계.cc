#include <iostream>
using namespace std;

int main() {
    int H, M;
    cin >> H >> M;

    if(M < 45){
       M += (60 - 45);
       H--;
    }
    else{
        M -= 45;
    }
    if(H < 0){
        H = 23;
    }
    cout << H << " " << M;
}

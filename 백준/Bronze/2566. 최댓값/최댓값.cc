#include <iostream>
using namespace std;

int main() {
    int arr[9][9];
    int max_v, max_r, max_c;
    max_v = -1;

    for(int i=0; i < 9; i++){
        for(int j=0; j < 9; j++){
            cin >> arr[i][j];
            if (arr[i][j] > max_v){
                max_v = arr[i][j];
                max_r = i+1;
                max_c = j+1;
            }
        }
    }
    cout << max_v << endl << max_r << " " << max_c;
}
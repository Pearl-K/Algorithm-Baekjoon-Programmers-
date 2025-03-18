#include <iostream>
#include <algorithm>
using namespace std;
int N;

int main(){
    cin.tie(0)->sync_with_stdio(0);
    while(true){
        cin >> N;
        if(N==0) break;

        int cnt = 0;
        bool flg = false;
        int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

        for(int i=1; i<10; ++i){
            if(flg) break;
            do {
                if(arr[0] != 0) cnt++;
                if(cnt == N){
                    for(int j=0; j<i; ++j) cout << arr[j];
                    cout << "\n";
                    flg = true;
                    break;
                }
                reverse(arr+i, arr+10);
            } while(next_permutation(arr, arr+10));
        }
    }
    return 0;
}
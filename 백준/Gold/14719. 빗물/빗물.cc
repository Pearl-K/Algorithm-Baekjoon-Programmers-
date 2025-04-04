#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int H, W;
int ret = 0;
int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> H >> W;
    vector<int> arr(W);
    for(int i=0; i <W; ++i) cin >> arr[i];  
    int st = 0;
    int ed = W-1;
    int l, r, tmp;

    while(st <= ed){
        tmp = min(arr[st], arr[ed]);
        l = st+1;
        r = ed;
        while(l < r){
            if(arr[l] < tmp){
                ret += tmp - arr[l];
                arr[l] = tmp;
            }
            l++;
        }
        if(tmp == arr[st]) st++;
        else ed--;
    }
    cout << ret;
    return 0;
}
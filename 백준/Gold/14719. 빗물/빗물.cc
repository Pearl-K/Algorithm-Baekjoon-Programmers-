#include <bits/stdc++.h>
using namespace std;
int H, W;
int ret = 0;
//빗물이 고이기 위해서는 시작점을 기준으로
//내려갔다 올라가는 형태인지 판단하면 된다.

int main() {
    cin.tie(0)->ios_base::sync_with_stdio(false);
    cin >> H >> W;
    vector<int> arr(W);

    for(int i=0; i <W; i++){
        cin >> arr[i];
    }

    int st = 0;
    int ed = W-1;
    int l, r, tmpMin;

    while(st <= ed){
        tmpMin = min(arr[st], arr[ed]);
        l = st+1; //l ~ r까지 구간 시작
        r = ed;

        while(l < r){
            if(arr[l] < tmpMin){
                ret += tmpMin - arr[l];
                arr[l] = tmpMin;
            }
            l++;
        }
        if(tmpMin == arr[st]) st++;
        else ed--;
    }
    cout << ret;
    return 0;
}
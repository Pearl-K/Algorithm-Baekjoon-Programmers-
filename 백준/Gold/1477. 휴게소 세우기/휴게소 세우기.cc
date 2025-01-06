#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int MAX = 1001;
int N, M, L;

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M >> L;

    vector<int> arr(N);
    for(int i = 0; i < N; i++) cin >> arr[i];
    arr.push_back(0);
    arr.push_back(L);
    sort(arr.begin(),arr.end());

    int st = 1;
    int ed = L-1;
    int mid;
    int ret = MAX;

    while(st <= ed){
        mid = (st+ed)/2;
        int tmpRet = 0;

        for(int i = 1; i < arr.size(); i++){
            int diff = arr[i] - arr[i-1];
            int cnt = diff / mid;
            if(cnt > 0){
                if(diff % mid == 0) tmpRet += cnt-1;
                else tmpRet += cnt;
            }
        }

        if(tmpRet > M){
            st = mid+1;
        }
        else{
            ed = mid-1;
            ret = min(ret,mid);
        }
    }
    cout << ret << "\n";
    return 0;
}
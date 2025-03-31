#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int N, D, K, C;
vector<int> arr;

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> D >> K >> C;

    for(int i=0; i<N; ++i) {
        int tmp;
        cin >> tmp;
        arr.push_back(tmp);
    }

    vector<int> vst(D+1);
    int res = 0;
    int cnt = 0;

    for(int i=0; i<K; ++i){
        if (!vst[arr[i]]) cnt += 1;
        vst[arr[i]] += 1;
    }
    res = cnt;

    for(int left=0; left<N; ++left){
        int right=(left+K)%N;
        int front = arr[left];
        int end = arr[right];

        vst[front] -= 1;
        if(!vst[front]) cnt -= 1;

        vst[end] += 1;
        if(vst[end]==1) cnt += 1;

        if(vst[C]==0) res = max(res, cnt+1);
        else res = max(res, cnt);
        if (res==K+1) break;
    }
    cout << res << "\n";
    return 0;
}
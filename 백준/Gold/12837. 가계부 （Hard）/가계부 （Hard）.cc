#include <iostream>
using namespace std;
using ll = long long;
const int MAX = (1e9)*2+1;
int N, Q;
ll sumTree[4000004];

ll updateTree(int st, int ed, int idx, int pos, int val){
    if(pos < st || pos > ed) return sumTree[idx];
    if(st == ed) return sumTree[idx] += val;
    int mid = (st + ed) >> 1;
    ll lval = updateTree(st, mid, idx << 1, pos, val);
    ll rval = updateTree(mid + 1, ed, idx << 1 | 1, pos, val);
    return sumTree[idx] = lval + rval;
}

ll querySum(int st, int ed, int qs, int qe, int idx){
    if(qe < st || ed < qs) return 0;
    if(qs <= st && ed <= qe) return sumTree[idx];
    int mid = (st+ed) >> 1;
    ll lval = querySum(st, mid, qs, qe, idx << 1);
    ll rval = querySum(mid+1, ed, qs, qe, idx << 1 | 1);
    return lval + rval;
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> Q;
    for(int i=0; i<Q; ++i){
        int comm, a, b;
        cin >> comm >> a >> b;
        if(comm == 1){
            updateTree(1, N, 1, a, b);
        } else{
            cout << querySum(1, N, a, b, 1) << "\n";
        }
    }
    return 0;
}
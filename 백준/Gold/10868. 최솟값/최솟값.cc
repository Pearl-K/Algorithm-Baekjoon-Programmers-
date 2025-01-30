#include <iostream>
using namespace std;
using ll = long long;
const int MAX = 1e9+1;
int N, M;
int arr[100001];
int minTree[400001];

int initTree(int st, int ed, int idx){
    if(st == ed) return minTree[idx] = arr[st];
    int mid = (st+ed) >> 1;
    int lval = initTree(st, mid, idx << 1);
    int rval = initTree(mid+1, ed, idx << 1 | 1);
    return minTree[idx] = min(lval, rval);
}

int findMin(int st, int ed, int qs, int qe, int idx){
    if(qe < st || ed < qs) return MAX;
    if(qs <= st && ed <= qe) return minTree[idx];
    int mid = (st+ed) >> 1;
    int lval = findMin(st, mid, qs, qe, idx << 1);
    int rval = findMin(mid+1, ed, qs, qe, idx << 1 | 1);
    return min(lval, rval);
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M;
    for(int i=1; i<=N; ++i) cin >> arr[i];

    fill(minTree, minTree+400001, MAX);
    initTree(1, N, 1);

    for(int i=0; i<M; ++i){
        int a, b;
        cin >> a >> b;
        cout << findMin(1, N, a, b, 1) << "\n";
    }
    return 0;
}
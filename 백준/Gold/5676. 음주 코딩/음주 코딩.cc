#include <iostream>
#include <cstring>
using namespace std;

int N, K;
int arr[100001];
int segTree[400001];

int initTree(int st, int ed, int idx) {
    if(st == ed) {
        if(arr[st] > 0) return segTree[idx] = 1;
        else if (arr[st] < 0) return segTree[idx] = -1;
        else return segTree[idx] = 0;
    }

    int mid = (st+ed) >> 1;
    int l = initTree(st, mid, idx << 1);
    int r = initTree(mid+1, ed, idx << 1 | 1);
    return segTree[idx] = l * r;
}

void updateTree(int st, int ed, int idx, int pos, int val) {
    if(pos < st || ed < pos) return;
    if(st == ed) {
        segTree[idx] = val;
        return;
    }
    
    int mid = (st+ed) >> 1;
    updateTree(st, mid, idx << 1, pos, val);
    updateTree(mid+1, ed, idx << 1 | 1, pos, val);
    segTree[idx] = segTree[idx << 1] * segTree[idx << 1 | 1];
}

int findVal(int st, int ed, int qs, int qe, int idx) {
    if(qe < st || ed < qs) return 1;
    if(qs <= st && ed <= qe) return segTree[idx];

    int mid = (st+ed) >> 1;
    int l = findVal(st, mid, qs, qe, idx << 1);
    int r = findVal(mid+1, ed, qs, qe, idx << 1 | 1);
    return l * r;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    while(cin >> N >> K) {
        memset(arr, 0, sizeof(arr));
        memset(segTree, 0, sizeof(segTree));

        for(int i=1; i<=N; ++i) cin >> arr[i];
        initTree(1, N, 1);
        string ret = "";

        for(int i=0; i<K; ++i) {
            char comm;
            int a, b;
            cin >> comm >> a >> b;
            if(comm == 'C') {
                int tmp = (b > 0) ? 1 : (b < 0 ? -1 : 0);
                updateTree(1, N, 1, a, tmp);
            }
            else {
                int tmp = findVal(1, N, a, b, 1);
                ret += (tmp > 0) ? "+" : (tmp < 0 ? "-" : "0");
            }
        }
        cout << ret << "\n";
    }
    return 0;
}

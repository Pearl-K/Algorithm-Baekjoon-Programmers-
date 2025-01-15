#include <iostream>
using namespace std;
using ll = long long;
const int MAX = 2000001;
int tree[1<<22];
int N, option, value;

void updateTree(int node, int s, int e, int idx, int val){
    if(e < idx || idx < s) return;
    if(s == e){
        tree[node] += val;
        return;
    }
    int mid = (s+e) >> 1;
    updateTree(node << 1, s, mid, idx, val);
    updateTree(node << 1 | 1, mid+1, e, idx, val);
    tree[node] = tree[node << 1] + tree[node << 1 | 1];
}

int getKth(int node, int s, int e, int k){
    tree[node] -=1;
    if(s == e) return s;
    int leftSize = tree[node << 1];
    int mid = (s + e) >> 1;
    
    if(k <= leftSize) return getKth(node << 1, s, mid, k);
    else return getKth(node << 1 | 1, mid+1, e, k-leftSize);
}

void update(int val){
    updateTree(1, 1, MAX, val, 1);
}

int query(int val){
    return getKth(1, 1, MAX, val);
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N;
    while(N--){
        cin >> option >> value;
        if(option == 1) update(value);
        else cout << query(value) << "\n";
    }
    return 0;
}
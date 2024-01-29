#include <iostream>
using namespace std;
const int INF = 1e9+1;
int N, Q;
int arr[100001];
int node[400001] = {INF,};

int init(int s, int e, int n){
    if (s==e) return node[n] = arr[s];
    int m = (s+e)/2;
    const int lval = init(s, m, 2*n);
    const int rval = init(m+1, e, 2*n+1);
    return node[n] = min(lval, rval);
}

int update(int i, int x, int n, int s, int e){
    if (e < i || i < s) return node[n];
    if (i <= s && e <= i) return node[n] = x;
    const int m = (s+e)/2;
    const int lval = update(i, x, 2*n, s, m);
    const int rval = update(i, x, 2*n+1, m+1, e);
    return node[n] = min(lval, rval);
}

int query(int qs, int qe, int n, int s, int e){
    if (e < qs || qe < s) return INF;
    if (qs <= s && e <= qe) return node[n];
    const int m = (s+e)/2;
    const int lval = query(qs, qe, 2*n, s, m);
    const int rval = query(qs, qe, 2*n+1, m+1, e);
    return min(lval, rval);
}

int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    for(int i=0; i < N; i++){
        cin >> arr[i];
    }
    init(0, N-1, 1);
    cin >> Q;
    for(int i=0; i < Q; i++){
        int com, a, b;
        cin >> com >> a >> b;

        if(com == 1) update(a-1, b, 1, 0, N-1);
        else cout << query(a-1, b-1, 1, 0, N-1) << '\n';
    }
    return 0;
}
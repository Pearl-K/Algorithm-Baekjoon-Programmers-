#include <iostream>
#include <algorithm>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
const int INF = 1000000000 + 1;

int N, M;
int arr[100001];
pii treeMin[400001]; // {value, index}

pii initMin(int s, int e, int n) {
    if (s==e) return treeMin[n] = {arr[s], s};
    int m = (s+e)/2;

    auto lval = initMin(s, m, 2*n);
    auto rval = initMin(m+1, e, 2*n+1);

    if (lval.first < rval.first || (lval.first == rval.first && lval.second < rval.second)) {
        return treeMin[n] = lval;
    } else {
        return treeMin[n] = rval;
    }
}

pii updateMin(int i, int x, int n, int s, int e) {
    if (e < i || i < s) return treeMin[n];
    if (s==e) return treeMin[n] = {x, s};
    int m = (s+e)/2;

    auto lval = updateMin(i, x, 2*n, s, m);
    auto rval = updateMin(i, x, 2*n+1, m+1, e);

    if (lval.first < rval.first || (lval.first == rval.first && lval.second < rval.second)) {
        return treeMin[n] = lval;
    } else {
        return treeMin[n] = rval;
    }
}

pii queryMin(int qs, int qe, int n, int s, int e) {
    if (e < qs || qe < s) return {INF, INF};
    if (qs <= s && e <= qe) return treeMin[n];
    int m = (s+e)/2;

    auto lval = queryMin(qs, qe, 2*n, s, m);
    auto rval = queryMin(qs, qe, 2*n+1, m+1, e);

    if (lval.first < rval.first || (lval.first == rval.first && lval.second < rval.second)) {
        return lval;
    } else {
        return rval;
    }
}

int main(void) {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    initMin(0, N-1, 1);

    cin >> M;
    for (int i = 0; i < M; i++) {
        int op;
        cin >> op;
        if (op == 2) { // Query
            int a, b;
            cin >> a >> b;
            auto minRet = queryMin(a-1, b-1, 1, 0, N-1);
            cout << minRet.second + 1 <<"\n";
        } else if (op == 1) { // Update
            int idx, val;
            cin >> idx >> val;
            updateMin(idx-1, val, 1, 0, N-1);
        }
    }
    return 0;
}
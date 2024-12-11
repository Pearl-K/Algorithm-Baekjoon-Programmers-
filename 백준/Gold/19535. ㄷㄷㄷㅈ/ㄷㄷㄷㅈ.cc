#include <iostream>
#include <vector>
using namespace std;
using ll = long long;
const int MAX = 300000; // 최대 정점 수
ll comb[4][MAX+1]; // 조합 전처리 값
int N;

// 조합 전처리 함수
void precomputeComb() {
    for (int r = 0; r <= 3; ++r) {
        for (int n = 0; n <= MAX; ++n) {
            if (r > n) comb[r][n] = 0;
            else if (r == 0 || r == n) comb[r][n] = 1;
            else comb[r][n] = comb[r-1][n-1] + comb[r][n-1];
        }
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N;
    vector<vector<int>> tree(N + 1);

    for (int i = 0; i < N-1; ++i) {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    // 조합 전처리
    precomputeComb();
    ll gCnt = 0, dCnt = 0;

    // ㅈ(G) 모양 계산
    for (int i = 1; i <= N; ++i) {
        int degree = tree[i].size();
        if (degree >= 3) {
            gCnt += comb[3][degree];
        }
    }

    // ㄷ(D) 모양 계산
    for (int u = 1; u <= N; ++u) {
        for (int v : tree[u]) {
            if (tree[u].size() > 1 && tree[v].size() > 1) {
                dCnt += (tree[u].size()-1) * (tree[v].size()-1);
            }
        }
    }

    // 간선 쌍이 중복 계산되므로 2로 나눠줌
    dCnt /= 2;

    if (dCnt > gCnt*3) cout << "D";
    else if (dCnt < gCnt*3) cout << "G";
    else cout << "DUDUDUNGA";

    return 0;
}
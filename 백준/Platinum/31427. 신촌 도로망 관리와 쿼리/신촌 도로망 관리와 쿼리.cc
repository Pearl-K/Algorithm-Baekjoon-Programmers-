#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <map>
using namespace std;
using pii = pair<int, int>;
using ll = long long;
const int MAX_WEIGTHS = 5;
ll N, M, Q;

struct UnionFind {
    vector<int> parent, cnt;
    UnionFind(int N = 0) : parent(N), cnt(N, 1) { iota(parent.begin(), parent.end(), 0);}

    int findParent(int x){
        if (parent[x] == x) return x;
        else return findParent(parent[x]);
    }

    bool unionParent(int x, int y){
        x = findParent(x);
        y = findParent(y);
        if (x == y) return false;
        if (cnt[x] < cnt[y]) swap(x, y);

        parent[y] = x;
        cnt[x] += cnt[y];
        return true;
    }

    int returnCnt(int x){
        return cnt[findParent(x)];
    }

    bool sameParent(int x, int y){
        return findParent(x) == findParent(y);
    }
};

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M >> Q;
    vector<pii> tree[5];

    for (int i=0; i < M; i++){
        int u, v;
        char z;
        cin >> u >> v >> z;
        tree[z-'A'].emplace_back(u-1, v-1);
    }
    array<int, MAX_WEIGTHS> univ = {0, 1, 2, 3, 4};
    map<array<int, MAX_WEIGTHS>, array<ll, MAX_WEIGTHS>> cntEdges;

    do {
        array<ll, MAX_WEIGTHS> now{};
        UnionFind UF(N);
        for (int i=0; i < MAX_WEIGTHS; i++){
            for (auto[u, v]: tree[univ[i]]) if (UF.unionParent(u, v)) now[univ[i]]++;
        }
        cntEdges[univ] = now;
    } while (next_permutation(begin(univ), end(univ)));

    while (Q--) {
        array<ll, MAX_WEIGTHS> W;
        for (int i=0; i < MAX_WEIGTHS; i++){
            cin >> W[i];
        }
        
        array<int, MAX_WEIGTHS> tmp {0, 1, 2, 3, 4};
        sort(begin(tmp), end(tmp), [&] (int i, int j) {return W[i] < W[j];});

        ll W_sum = 0;
        auto Ecnt = cntEdges[tmp];

        for (int i=0; i < MAX_WEIGTHS; i++){
            W_sum += W[i]*Ecnt[i];
        }
        cout << W_sum << '\n';
    }
    return 0;
}
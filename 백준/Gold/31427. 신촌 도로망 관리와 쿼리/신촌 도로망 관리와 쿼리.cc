#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <map>

using namespace std;
using ll = long long;
const int MAX_WEIGTHS = 5;
ll N, M, Q;

// 에디토리얼의 UnionFind 구조체와 map을 참고했습니다

struct UnionFind {

    //배열 선언 후, <numeric>의 iota 함수를 통해 순차적인 값을 할당하여 초기화
    vector<int> parent, cnt;
    UnionFind(int N = 0) : parent(N), cnt(N, 1) { iota(parent.begin(), parent.end(), 0);}

    int find_p (int x){
        if (parent[x] == x) return x;
        else return find_p(parent[x]);
    }

    bool unite (int x, int y) {
        x = find_p(x);
        y = find_p(y);

        if (x == y) return false;
        if (cnt[x] < cnt[y]) swap(x, y);

        parent[y] = x;
        cnt[x] += cnt[y];
        return true;
    }

    int return_cnt (int x) {
        return cnt[find_p(x)];
    }

    bool same_p (int x, int y){
        return find_p(x) == find_p(y);
    }

};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M >> Q;
    vector<pair<int, int>> tree[5];


    for (int i=0; i < M; i++){
        int u, v;
        char z;
        cin >> u >> v >> z;
        tree[z-'A'].emplace_back(u-1, v-1);
    }

    // A B C D E 순서의 univ
    // std:: array와 std:: vector의 차이 체크
    array<int, MAX_WEIGTHS> univ = {0, 1, 2, 3, 4};
    map<array<int, MAX_WEIGTHS>, array<ll, MAX_WEIGTHS>> cntEdges;

    do {
        array<ll, MAX_WEIGTHS> now{};
        UnionFind UF(N);

        for (int i=0; i < MAX_WEIGTHS; i++){
            for (auto[u, v]: tree[univ[i]]) if (UF.unite(u, v)) now[univ[i]]++;
        }
        cntEdges[univ] = now; //map cntEdges에 할당하는 구조

    } while (next_permutation(begin(univ), end(univ)));


    while (Q--) {
        array<ll, MAX_WEIGTHS> W;
        for (int i=0; i < MAX_WEIGTHS; i++){
            cin >> W[i];
        }

        //array tmp를 가중치 배열인 W의 크기 순서대로 정렬
        array<int, MAX_WEIGTHS> tmp {0, 1, 2, 3, 4};
        sort(begin(tmp), end(tmp), [&] (int i, int j) {return W[i] < W[j];});

        //순서대로 정렬한 tmp를 가지고 기존 map cntEdges에서 간선 cnt 개수 찾기
        ll W_sum = 0;
        auto Ecnt = cntEdges[tmp];

        for (int i=0; i < MAX_WEIGTHS; i++){
            W_sum += W[i]*Ecnt[i];
        }
        cout << W_sum << '\n';
    }
    return 0;
}

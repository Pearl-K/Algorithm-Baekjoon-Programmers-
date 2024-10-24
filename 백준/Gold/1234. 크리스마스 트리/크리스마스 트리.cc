#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

ll N, R, G, B;
ll fact[12];
ll treedp[12][111][111][111];

void fact_dp() {
    fact[0] = 1;
    for (int i = 1; i <= 11; i++) {
        fact[i] = i * fact[i-1];
    }
}

ll comb(ll n, ll r) {
    if (r == 2) return fact[n] / fact[n/2] / fact[n/2];
    if (r == 3) return fact[n] / fact[n/3] / fact[n/3] / fact[n/3];
}

ll dfs(int depth, int r, int g, int b) {

    // 개수 조건이 맞지 않다면 false==0 을 반환한다
    if (depth == N+1) return (r <= R && g <= G && b <= B);

    // 찾는 값이 dp에 정의되어 있을 때
    ll& ret = treedp[depth][r][g][b];
    if (~ret) return ret;
    ret = 0;

    // 1. 한 가지 색으로 채울 때 = depth만큼 사용한 개수를 늘린다
    ret += dfs(depth+1, r + depth, g, b);
    ret += dfs(depth+1, r, g + depth, b);
    ret += dfs(depth+1, r, g, b + depth);

    // 2. depth가 2로 나누어 떨어질 때, 두 가지 색을 사용할 수 있다.
    if (depth % 2 == 0) {
        ret += dfs(depth+1, r + depth/2, g+depth/2, b) * comb(depth, 2);
        ret += dfs(depth+1, r + depth/2, g, b+depth/2) * comb(depth, 2);
        ret += dfs(depth+1, r, g + depth/2, b+depth/2) * comb(depth, 2);
    }

    // 3. depth가 3으로 나누어 떨어질 때, 세 가지 색을 사용할 수 있다.
    if (depth % 3 == 0) {
        ret += dfs(depth+1, r+depth/3, g+depth/3, b+depth/3) * comb(depth, 3);
    }

    return ret;
}

int main() {
    cin.tie(0)->ios::sync_with_stdio(false);

    cin >> N >> R >> G >> B;

    memset(treedp, -1, sizeof(treedp));
    fact_dp();
    cout << dfs(1, 0, 0, 0) << '\n';
}
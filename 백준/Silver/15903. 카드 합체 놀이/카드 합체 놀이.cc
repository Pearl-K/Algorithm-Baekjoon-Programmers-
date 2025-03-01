#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using ll = long long;

int N, M;
ll arrSum = 0;
priority_queue<ll, vector<ll>, greater<ll>> PQ;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M;
    for(int i = 0; i < N; ++i) {
        ll x;
        cin >> x;
        arrSum += x;
        PQ.push(x);
    }

    while (M--) {
        ll a = PQ.top();
        PQ.pop();
        ll b = PQ.top();
        PQ.pop();
        ll tmp = a + b;
        arrSum += tmp;
        PQ.push(tmp);
        PQ.push(tmp);
    }
    cout << arrSum << "\n";
    return 0;
}
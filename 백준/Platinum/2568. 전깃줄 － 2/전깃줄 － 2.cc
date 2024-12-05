#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;
using pi = pair<int, int>;
int n;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n;
    vector<pi> lis;

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        lis.emplace_back(a, b);
    }

    sort(lis.begin(), lis.end());
    vector<int> dp;
    vector<int> position(n, -1);
    vector<int> trace(n, -1);

    for (int i = 0; i < n; i++) {
        int b = lis[i].second;

        auto it = lower_bound(dp.begin(), dp.end(), b);
        int pos = it - dp.begin();

        if (it == dp.end()) {
            dp.push_back(b);
        } else {
            *it = b;
        }
        position[pos] = i;
        if (pos > 0) {
            trace[i] = position[pos-1];
        }
    }

    cout << n - dp.size() << "\n";

    vector<int> lisTrace;
    int cur = position[dp.size() - 1];
    while (cur != -1) {
        lisTrace.push_back(lis[cur].first);
        cur = trace[cur];
    }

    unordered_set<int> lisSet(lisTrace.begin(), lisTrace.end());
    vector<int> ret;

    for(const auto& p: lis){
        if(lisSet.find(p.first) == lisSet.end()) ret.push_back(p.first);
    }
    sort(ret.begin(), ret.end());

    for(int r: ret) cout << r << "\n";
    return 0;
}
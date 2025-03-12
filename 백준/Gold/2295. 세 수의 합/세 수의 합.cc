#include <iostream>
#include <set>
#include <algorithm>
using namespace std;
using ll = long long;

set<ll> finds;
ll N;
ll arr[1001];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N;
    for(int i=0; i<N; ++i) cin >> arr[i];
    for(int i=0; i<N; ++i) {
        for(int j=i; j<N; ++j) {
            finds.insert(arr[i]+arr[j]);
        }
    }
    
    sort(arr, arr+N);
    ll ret = 0;
    bool found = false;
    for (int i=N-1; i>=0 && !found; --i) {
        for (int j=0; j<N; ++j) {
            ll target = arr[i]-arr[j];
            if (finds.count(target)) {
                ret = arr[i];
                found = true;
                break;
            }
        }
    }
    cout << ret << "\n";
    return 0;
}
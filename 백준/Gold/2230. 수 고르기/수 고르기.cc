#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;
using pi = pair<int, int>;
const int MAX = 2000000001;
int n;
ll m;
vector<ll> arr;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m;
    for(int i=0; i<n; i++) {
        ll num;
        cin >> num;
        arr.push_back(num);
    }
    sort(arr.begin(), arr.end());

    int st = 0;
    int ed = 0;
    ll ret = MAX;

    while (st <= ed && ed < n){
        ll target = arr[ed] - arr[st];

        if(target >= m){
            ret = min(ret, target);
            st++;
        }
        else ed++;
    }

    cout << ret << "\n";
    return 0;
}
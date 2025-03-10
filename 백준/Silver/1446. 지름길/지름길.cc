#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
const int MAX = 1e9;
using pii = pair<int, int>;
vector<pii> arr[10001];
int N, D;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> D;

    int u, v, w;
    for(int i=0; i<N; ++i){
        cin >> u >> v >> w;
        arr[v].push_back(make_pair(u, w));
    }

    vector<int> ret(D+1, MAX);
    ret[0] = 0;
    for(int i=1; i<=D; ++i){
        if(arr[i].size() == 0) ret[i] = ret[i-1]+1;
        else {
            for (pii nxt: arr[i]) ret[i] = min(ret[i], min(ret[i-1]+1, ret[nxt.first]+nxt.second));
        }
    }
    cout << ret[D] << "\n";
    return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using pii = pair<int, int>;

int N, st, ed;
vector<pii> adj[100001];
bool vst[100001] = {false, };
bool flag = false;

void dfs(int now, int sum, int maxDist) {
	if (flag) return;
	if (now == ed) {
		cout << sum-maxDist << "\n";
		flag = true;
		return;
	}

	for (int i=0; i < adj[now].size(); ++i) {
		int nnode = adj[now][i].first;
		int ndist = adj[now][i].second;
		if (!vst[nnode]) {
			vst[nnode] = true;
			dfs(nnode, sum+ndist, max(ndist, maxDist));
		}
	}
	return;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> st >> ed;
    for(int i=0; i < N-1; ++i){
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
	vst[st] = true;
	dfs(st, 0, 0);
	return 0;
}
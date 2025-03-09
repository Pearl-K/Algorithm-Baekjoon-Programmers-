#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;
const int MAX = 100001;
int N, M;
vi tree[MAX];
int prs[MAX];
int dp[MAX];

void dfs(int now) {
	for (int nxt : tree[now]) {
		if (prs[now] == nxt) continue;
		dp[nxt] += dp[now];
		dfs(nxt);
	}
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
	cin >> N >> M;

	for(int i=1; i<=N; ++i) {
		int num;
		cin >> num;
		prs[i] = num;
		if (num != -1) {
			tree[num].push_back(i);
			tree[i].push_back(num);
		}
	}
	for(int i=0; i<M; ++i) {
		int a, b;
		cin >> a >> b;
		dp[a] += b;		
	}
	dfs(1);
	for(int i=1; i<=N; ++i) cout << dp[i] << " ";
}
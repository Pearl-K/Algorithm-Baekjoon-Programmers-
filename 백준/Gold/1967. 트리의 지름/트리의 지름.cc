#include <bits/stdc++.h>
#define MAX 10001
using namespace std;

int n;
int a, b, w;
vector<pair<int, int>> tree[MAX];
int dist[MAX];

void dfs(int u, int w){
    for (const pair<int, int>& node : tree[u]) {
        int now_n = node.first;
        int now_w = node.second;
        if (dist[now_n] == -1) {
            dist[now_n] = now_w + w;
            dfs(now_n, now_w + w);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for(int i=0; i < n-1; i++){
        cin >> a >> b >> w;
        tree[a].push_back(make_pair(b, w));
        tree[b].push_back(make_pair(a, w));
    }

    memset(dist, -1, sizeof(dist));
    dist[1] = 0;
    dfs(1, 0);

    int max_i = 1;
    for(int i=2; i <= n; i++){
        if (dist[i] > dist[max_i]){
            max_i = i;
        }
    }

    memset(dist, -1, sizeof(dist));
    dist[max_i] = 0;
    dfs(max_i, 0);

    int ret = 0;
    for(int i =1; i <= n; ++i){
        ret = max(ret, dist[i]);
    }

    cout << ret;
    return 0;
}
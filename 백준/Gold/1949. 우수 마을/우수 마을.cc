#include <iostream>
#include <vector>
using namespace std;
typedef pair<int, int> pii;

int N;
vector<vector<int>> graph;
bool visited[10001] = {false, };
int val[10001];
int dp[2][10001];

void dfs(int node){
    visited[node] = true;
    dp[0][node] = 0;
    dp[1][node] = val[node];

    for(auto &next: graph[node]){
        if(!visited[next]){
            dfs(next);
            dp[0][node] += max(dp[0][next], dp[1][next]);
            dp[1][node] += dp[0][next];
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    graph.resize(N+1);

    for(int i=1; i <= N; i++){
        cin >> val[i];
    }

    for(int i=0; i < N-1; i++){
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int ret;
    dfs(1);
    ret = max(dp[0][1], dp[1][1]);
    cout << ret;
    return 0;
}
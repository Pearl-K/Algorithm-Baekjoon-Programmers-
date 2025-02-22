#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pllpii = pair<ll, pii>;
const ll INF = 1e15;
int N, M, K; // 노드, 엣지, 포장 도로 수
ll dp[21][10001]; // 포장 수에 따른 dp
vector<vector<pii>> adj;

void dijkstra(int st){
    priority_queue<pllpii, vector<pllpii>, greater<pllpii>> pq;
    pq.push({0, {st, 0}});

    while(!pq.empty()){
        ll cost = pq.top().first;
        int node = pq.top().second.first;
        int kUsed = pq.top().second.second;
        pq.pop();

        if(dp[kUsed][node] < cost) continue;

        for(auto nxt: adj[node]){
            ll nxtCost = nxt.first;
            int nxtNode = nxt.second;

            ll newCost = cost + nxtCost;
            if(newCost < dp[kUsed][nxtNode]){
                dp[kUsed][nxtNode] = newCost;
                pq.push({newCost, {nxtNode, kUsed}});
            }

            if(kUsed < K){
                ll newCost = cost; // cost + 0 처리
                if(newCost < dp[kUsed+1][nxtNode]){
                    dp[kUsed+1][nxtNode] = newCost;
                    pq.push({newCost, {nxtNode, kUsed+1}});
                }
            }
        }
    }
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M >> K;
    adj.resize(N+1);
    for(int i=0; i<M; ++i){
        int st, ed, w;
        cin >> st >> ed >> w;
        adj[st].push_back({w, ed});
        adj[ed].push_back({w, st});
    }

    for(int k=0; k<=K; ++k) for(int v=1; v<=N; ++v) dp[k][v] = INF;
    dp[0][1] = 0; //시작점 초기화
    dijkstra(1);
    
    ll ret = INF;
    for(int k=0; k<=K; ++k) ret = min(ret, dp[k][N]);
    cout << ret << "\n";
    return 0;
}
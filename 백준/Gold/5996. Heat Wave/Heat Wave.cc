#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using ll = long long;
const int INF = 1e9 + 7;

int T, C, S, E;
vector<pair<int, int>> graph[2501];


ll dijkstra(int start, int end){
    vector<ll> dist(T+1, INF);
    dist[start] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> PQ;
    PQ.push({0, start}); // dist, node 순서

    while(!PQ.empty()){
        int cost = PQ.top().first;
        int node = PQ.top().second;
        PQ.pop();

        for(int i=0; i < graph[node].size(); i++){
            int now_c = graph[node][i].first;
            int now_n = graph[node][i].second;

            if(dist[node] < cost) continue;

            if(dist[now_n] > now_c + cost){
                dist[now_n] = now_c + cost;
                PQ.push({dist[now_n], now_n});
            }
        }
    }
    if (dist[end] == INF) return -1;
    else return dist[end];
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> T >> C >> S >> E;

    for(int c=0; c < C; c++){
        int u, v, w;
        cin >> u >> v >> w;

        graph[u].push_back({w, v}); //cost, node 순서
        graph[v].push_back({w, u});
    }
    ll ret = dijkstra(S, E);
    cout << ret << "\n";
    return 0;
}
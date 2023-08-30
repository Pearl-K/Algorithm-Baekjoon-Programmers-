#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using ll = long long;
const int INF = 1e9 + 7;

int N, K;
vector<pair<int, int>> graph[101];


ll dijkstra(int start, int end){
    vector<ll> dist(N+1, INF);
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

    cin >> N >> K;

    for(int k=0; k < K; k++){
        int com; //command
        cin >> com;

        if(com==0){
            int a, b;
            cin >> a >> b;
            ll ret = dijkstra(a, b);
            cout << ret << "\n";

        } else{
            int c, d, e;
            cin >> c >> d >> e;
            graph[c].push_back({e, d}); //cost, node 순서
            graph[d].push_back({e, c});
        }
    }
}
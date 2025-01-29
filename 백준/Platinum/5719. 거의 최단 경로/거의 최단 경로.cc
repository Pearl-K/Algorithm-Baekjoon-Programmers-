#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;
using vpii = vector<pii>;

const int INF = 1e9;
int N, M;
int adj[501][501];
vi prevPath[501];

int dijkstra(int st, int ed) {
    vi dist(501, INF);
    dist[st] = 0;

    priority_queue<pii, vpii, greater<pii>> pq;
    pq.emplace(0, st);

    while(!pq.empty()) {
        int cost = pq.top().first;
        int node = pq.top().second;
        pq.pop();

        if(cost > dist[node]) continue;

        for(int i=0; i<501; ++i) {
            if (adj[node][i] != -1) {
                int nxtc = adj[node][i];
                int nxtn = i;

                if(dist[nxtn] > nxtc + cost) {
                    dist[nxtn] = nxtc + cost;
                    pq.emplace(dist[nxtn], nxtn);
                    prevPath[nxtn].clear();
                    prevPath[nxtn].push_back(node);
                }
                else if(dist[nxtn] == nxtc + cost) {
                    prevPath[nxtn].push_back(node);
                }
            }
        }
    }
    return (dist[ed] == INF) ? -1 : dist[ed];
}

// 종료 지점부터 역추적하면서 큐에 넣고 제거
void removeSP(int ed) {
    queue<int> q;
    q.push(ed);
    bool vst[501] = {false, };

    while(!q.empty()) {
        int node = q.front();
        vst[node] = true;
        q.pop();

        for(int pNode : prevPath[node]) {
            adj[pNode][node] = -1;

            if(!vst[pNode]) {
                q.push(pNode);
            }
        }
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M;

    while(N != 0 && M !=0) {
        int S, D, u, v, w;
        cin >> S >> D;

        // init
        memset(adj, -1, sizeof(adj));
        for(int i=0; i<501; ++i) prevPath[i].clear();

        for(int i=0; i<M; ++i) {
            cin >> u >> v >> w;
            adj[u][v] = w;
        }

        int SP = dijkstra(S, D);
        if(SP == -1) cout << -1 << "\n";
        else {
            removeSP(D);
            int nxtSP = dijkstra(S, D);
            cout << nxtSP << "\n";
        }
        cin >> N >> M;
    }
    return 0;
}
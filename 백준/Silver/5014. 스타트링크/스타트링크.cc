#include <iostream>
#include <vector>
#include <queue>
using namespace std;
 
const int MAX = 1000001;
int F, S, G, U, D;
int dist[MAX];
bool vst[MAX];
int dx[2];
queue<int> q;

void bfs(int node) {
    vst[node] = true;
    q.push(node);
 
    while (!q.empty()) {
        node = q.front();
        q.pop();
        
        for (int i = 0; i < 2; i++) {
            int nn = node + dx[i];
 
            if (0 < nn && nn <= F) {
                if (!vst[nn]) {
                    vst[nn] = true;
                    q.push(nn);
                    dist[nn] = dist[node] + 1;
                }
            }
        }
        
    }
}
 
int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> F >> S >> G >> U >> D;
    dx[0] = U;
    dx[1] = -D; 
    bfs(S);
 
    if (vst[G]) cout << dist[G];
    else cout << "use the stairs";
    return 0;
}
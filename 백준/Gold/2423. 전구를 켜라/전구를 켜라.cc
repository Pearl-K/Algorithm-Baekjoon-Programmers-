#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m;
const int INF = 1e9;
vector<vector<vector<pair<int, pair<int, int>>>>> grid;

int dijkstra(int x, int y){
    vector<vector<int>> dist(n+1, vector<int>(m+1, INF));
    priority_queue<pair<int, pair<int, int>>> PQ;

    dist[y][x] = 0;
    PQ.push({0, {x, y}});

    while (!PQ.empty()) {
        int cnt = -PQ.top().first;
        int x = PQ.top().second.first;
        int y = PQ.top().second.second;
        PQ.pop();

        if (dist[y][x] < cnt) continue;

        for (const auto &edge : grid[y][x]) {
            int nx = edge.second.first;
            int ny = edge.second.second;
            int new_dist = cnt + edge.first;

            if (dist[ny][nx] > new_dist) {
                dist[ny][nx] = new_dist;
                PQ.push({-new_dist, {nx, ny}});
            }
        }
    }
    int ret = dist[n][m];
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    grid.resize(n+1, vector<vector<pair<int, pair<int, int>>>>(m+1));

    for (int i=0; i < n; i++){
        string line;
        cin >> line;
        for (int j=0; j < m; j++){
            if (line[j] == '/') { //여기도 x, y 순서 조심
                grid[i][j+1].push_back({0, {j, i+1}});
                grid[i+1][j].push_back({0, {j+1, i}});
                grid[i][j].push_back({1, {j+1, i+1}});
                grid[i+1][j+1].push_back({1, {j, i}});
            } else {
                grid[i][j].push_back({0, {j+1, i+1}});
                grid[i+1][j+1].push_back({0, {j, i}});
                grid[i][j+1].push_back({1, {j, i+1}});
                grid[i+1][j].push_back({1, {j+1, i}});
            }
        }
    }
    int ret = dijkstra(0, 0);
    if (ret < INF) {
        cout << ret;
    } else {
        cout << "NO SOLUTION";
    }
    return 0;
}
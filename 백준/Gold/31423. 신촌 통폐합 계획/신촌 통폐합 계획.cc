#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int N;
bool vst[500001]= {false, };
vector<string> univ;
vector<vector<int>> tree;
vector<int> degree;
vector<int> res;

void dfs(int node){
    res.push_back(node);
    for (int next : tree[node]) {
        if (!vst[next]) {
            dfs(next);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    univ.resize(N + 1);
    tree.resize(N + 1);
    degree.resize(N + 1);

    for (int i = 1; i <= N; ++i) {
        cin >> univ[i];
    }

    for (int i=0; i < N-1; i++){
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        degree[v]++;
    }

    for (int i = 1; i <= N; ++i) {
        if (degree[i] == 0) {
            dfs(i);
        }
    }
    string res_s;
    for (int idx : res) {
        res_s += univ[idx];
    }
    cout << res_s;
    return 0;
}
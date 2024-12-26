#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vll = vector<ll>;

bool vst[300001];
ll ret = 0;

void dfs(vll &tree, vector<vi> &graph, int prev){
    vst[prev]=true;
    
    for(int i=0; i<graph[prev].size(); ++i){
        if(vst[graph[prev][i]]) continue;
        
        dfs(tree,graph,graph[prev][i]);
        ret += abs(tree[graph[prev][i]]);
        tree[prev] += tree[graph[prev][i]];
    }
}

ll solution(vector<int> a, vector<vector<int>> edges) {
    vll tree(a.begin(),a.end()); // copy
    vector<vi> graph(a.size()); // size 대로 그래프 제작
    int SIZE = edges.size();

    for(int i=0; i<SIZE; ++i){
        graph[edges[i][0]].push_back(edges[i][1]);
        graph[edges[i][1]].push_back(edges[i][0]);
    }

    dfs(tree,graph,0);

    if(tree[0] != 0) return -1;
    else return ret;
}
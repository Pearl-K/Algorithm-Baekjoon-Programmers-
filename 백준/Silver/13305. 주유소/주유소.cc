#include <iostream>
using namespace std;
using ll = long long;
int n;
int dist[100001];
int cost[100001];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n;
    for (int i = 0; i < n - 1; i++) cin >> dist[i];
    for (int i = 0; i < n; i++) cin >> cost[i];
    ll ret = cost[0] * dist[0];
    ll minCost = cost[0];

    for(int i = 1; i < n-1; i++){
        if(cost[i] < minCost){
            minCost = cost[i];
        }
        ret += minCost * dist[i];
    }
    cout << ret;
    return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
const int INF = 1e9;
int N;
int W[17][17];
int dp[17][1<<17];

int tsp(int idx, int vst) {
    if(vst == (1 << N)-1) {
        return W[idx][0] ? W[idx][0] : INF; //경로 없는 경우 체크
    }
    
    int &ret = dp[idx][vst];
    if(ret != -1) return ret; // updated 된 dp값 반환
    
    ret = INF;
    for(int i=0; i<N; ++i) {
        if(!(vst & (1 << i)) && W[idx][i] != 0) {
            ret = min(ret, tsp(i, vst | (1 << i)) + W[idx][i]);
        }
    }
    return ret;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N;
    for(int i=0; i<N; ++i)
        for(int j=0; j<N; ++j)
            cin >> W[i][j];

    memset(dp, -1, sizeof(dp));
    cout << tsp(0, 1) << "\n"; // 0번 root, 시작점 방문했으므로 0번째 비트 on
    return 0;
}
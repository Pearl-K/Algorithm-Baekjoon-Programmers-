#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define MAX 500001

vector<int> tree[MAX];
int N, color[MAX][3];
ll dp[MAX][3];
char ret[MAX];

// DP 테이블 갱신 함수
ll makeDP(int p, int q, int r){

    ll& ptr(dp[p][q]);
    if (!~ptr){
        ptr = color[p][q];
        for (int& i : tree[p])
            if (i ^ r){
                if (!q) ptr += max(makeDP(i, 1, p), makeDP(i, 2, p));
                else if (q & 1) ptr += max(makeDP(i, 0, p), makeDP(i, 2, p));
                else ptr += max(makeDP(i, 0, p), makeDP(i, 1, p));
            }
    }
    return ptr;
}

// 결과 Char 값 역추적
void trackChar(int x, int y, int z){
    ret[x] = y ? ( y > 1 ? 'B' : 'G') : 'R';

    for (int&i : tree[x]){
        if (i ^ z){
            if (!y) trackChar(i, dp[i][1] > dp[i][2] ? 1 : 2, x);
            else if (y & 1) trackChar(i, dp[i][0] > dp[i][2] ? 0 : 2, x);
            else trackChar(i, dp[i][1] > dp[i][0], x);
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;

    //1. tree 관계 입력 받기
    int u, v;
    for(int i=0; i < N-1; i++){
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    //2. color 순서 입력 받기
    int r, g, b;
    for(int i=1; i <=N; i++){
        cin >> color[i][0] >> color[i][1] >> color[i][2];
    }

    //3. DP table max 값 출력
    memset(dp, -1, sizeof dp);
    cout << max({makeDP(1, 0, 1), makeDP(1, 1, 1), makeDP(1, 2, 1)}) << "\n";

    //4. DP 값을 통한 char result 역추적
    trackChar(1, dp[1][dp[1][1] > dp[1][0]] > dp[1][2] ? dp[1][1] > dp[1][0] : 2, 1);

    for (int i=1; i<= N; i++){
        cout << ret[i];
    }
    
    cout << "\n";
    return 0;
}
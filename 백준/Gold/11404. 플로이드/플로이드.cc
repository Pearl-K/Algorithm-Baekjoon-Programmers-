#include <bits/stdc++.h>
#define INF 2147483647
using namespace std;
using ll = long long;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;

    cin >> N;
    cin >> M;
    ll graph[N+1][N+1];

    //배열 초기화
    for(int i =0; i <= N; i++){
        for(int j=0; j <= N; j++) {
            graph[i][j] = INF;
        }
    }

    for(int i =0; i < M; i++){
        int u, v, w;
        cin >> u >> v >> w;
        if (graph[u][v] > w) graph[u][v] = w; //여러 가지 간선이 있을 경우를 고려
    }


    //플로이드 워셜
    for(int k=1; k <= N; k++){
        for(int p=1; p <= N; p++){
            for(int q=1; q <= N; q++){
                if (p != q && graph[p][k] + graph[k][q] < graph[p][q]){
                    graph[p][q] = graph[p][k] + graph[k][q];
                }
            }
        }
    }

    //정답 출력
    for (int i=1; i <= N; i++){
        for (int j=1; j <=N; j++){
            if (graph[i][j] >= INF) {
                cout << 0 << " ";
            }else{
                cout << graph[i][j] << " ";
            }
        }
        cout << "\n";
    }
    return 0;
}
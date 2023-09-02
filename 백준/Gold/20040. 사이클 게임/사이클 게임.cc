#include <iostream>
using namespace std;
int N, M;
int ret = 0;
int parent[500000];

int find_p(int x){
    if(parent[x] != x){
        parent[x] = find_p(parent[x]);
    }
    return parent[x];
}

void union_p(int x, int y){
    int X, Y;
    X = find_p(x);
    Y = find_p(y);

    if(X > Y){
        parent[X] = Y;
    } else {
        parent[Y] = X;
    }
    return;
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;

    for(int i=0; i < N; i++){ //부모 배열 초기화
        parent[i] = i;
    }

    for(int m=0; m < M; m++){
        int u, v, up, vp;
        cin >> u >> v;

        up = find_p(u);
        vp = find_p(v);

        if (up == vp) {
            ret = m+1;
            break;
        }
        union_p(u, v);
    }
    cout << ret << "\n";
    return 0;
}
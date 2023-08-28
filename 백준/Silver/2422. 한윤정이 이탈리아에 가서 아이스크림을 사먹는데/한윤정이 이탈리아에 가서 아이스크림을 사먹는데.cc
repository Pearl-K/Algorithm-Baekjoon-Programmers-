#include <iostream>
using namespace std;
int N, M;
int w_c[201][201];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;

    for(int i=0; i < M; i++){
        int a, b;
        cin >> a >> b;
        w_c[a][b] = 1;
        w_c[b][a] = 1;
    }

    int ret = 0;
    for(int i=1; i <=N; ++i){
        for(int j=i+1; j <=N; ++j){
            if(w_c[i][j] == 1) continue;
            for(int l=j+1; l <=N; ++l){
                if(w_c[i][l] == 1 || w_c[j][l] == 1) continue;
                ret++;
                //cout << i << j << l << ret;
                //cout << "\n";
            }
        }
    }
    cout << ret;
    return 0;
}
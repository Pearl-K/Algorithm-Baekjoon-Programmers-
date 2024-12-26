#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;

/* 문제 접근
    기존 ranks는 순서 확인용으로 두고,
    기존 ranks 배열을 기준으로 DAG를 만든다
    해당 DAG를 가지고 M개의 주어진 명령들의 연결 관계를 역전시키면서
    그래프의 상태를 본다.
    -> inDegree == 0 인게 여러개 있는 경우 (순서 정립 불가)
    -> Cycle이 있는 경우 (순위 정하기 Impossible)
    -> 순서 확립이 되는 경우는 결과를 출력하면 된다.

    위상정렬 판단은 DFS 방식과 BFS 방식 모두 사용가능할듯?
*/

int T, N, M;
int ranks[501];
int inDegree[501];
bool adj[501][501];

void init(){
    for(int i=1; i<=500; ++i){
        ranks[i] = 0;
        inDegree[i] = 0;
        for(int j=1; j<=500; ++j) {
            adj[i][j] = false;
        }
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> T;

    while(T--){
        cin >> N;
        init();

        for(int i=1; i<=N; ++i) cin >> ranks[i];
        for(int i=1; i<=N; ++i) {
            for(int j=1; j<i; ++j) {
                adj[ranks[j]][ranks[i]] = true;
                inDegree[ranks[i]]++;
            }
        }

        cin >> M;
        for(int i=0; i<M; ++i){
            int a, b;
            cin >> a >> b;
            if(adj[a][b]) {
                adj[a][b] = false;
                adj[b][a] = true;
                inDegree[a]++;
                inDegree[b]--;
            }
            else if(adj[b][a]) {
                adj[b][a] = false;
                adj[a][b] = true;
                inDegree[b]++;
                inDegree[a]--;
            }
        }

        queue<int> Q;
        for(int i=1; i<=N; ++i) if(inDegree[i] == 0) Q.push(i);

        vi newRanks;
        bool isPossible = true;
        bool isOneRet = true;

        for(int i=0; i<N; ++i){
            if(Q.empty()){
                isPossible = false;
                break;
            }
            int now = Q.front();
            Q.pop();

            if(Q.size() > 0){
                isOneRet = false;
            }else{
                newRanks.push_back(now);
            }

            for(int j=1; j<=500; ++j){
                if(adj[now][j])
                    if(--inDegree[j] == 0)
                        Q.push(j);
            }
        }

        if(!isPossible) cout << "IMPOSSIBLE\n";
        else if(!isOneRet) cout << "?\n";
        else {
            for(int i=0; i<N ; ++i) cout << newRanks[i] << " ";
            cout << "\n";
        }
    }
    return 0;
}
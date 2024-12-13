#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using ll = long long;
using vi = vector<int>;
using pipii= pair<int, pair<int, int>>;
int N;
ll ret[10];
vector<pipii> graph[10];

ll GCD(ll a, ll b){
    if (b==0) return a;
    return GCD(b, a%b);
}

ll LCM(ll a, ll b){
    return a*b/GCD(a, b);
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N;

    ll totalLCM = 1;
    for(int i=0; i<N-1; ++i){
        int a, b, p, q;
        cin >> a >> b >> p >> q;

        graph[a].push_back({b, {p, q}});
        graph[b].push_back({a, {q, p}});
        totalLCM *= LCM(p, q);
    }

    // BFS, 0번 기준으로 시작하기
    ret[0] = totalLCM;
    queue<int> Q;
    Q.push(0);

    while(!Q.empty()){
        int now = Q.front();
        Q.pop();

        // <first, <seconde.first, second.seconde>> == <다음 노드,  <p, q>>
        for(auto nxt: graph[now]){
            if(ret[nxt.first]) continue;
            ret[nxt.first] = (ret[now] * nxt.second.second) / nxt.second.first;
            Q.push(nxt.first); // 다음 노드 넣기
        }
    }

    ll retGCD = ret[0];
    for(int i=1; i<N; ++i) retGCD = GCD(retGCD, ret[i]); //retGCD 찾기

    //마지막에 GCD로 나눠서 가장 간단한 정수 비율 찾기
    for(int i=0; i<N; ++i) cout << ret[i]/retGCD << " ";
    return 0;
}
#include <iostream>
#include <unordered_set>
using namespace std;
int N, K;
int arr[11];
bool vst[11];
unordered_set<int> ret;

void dfs(int depth, string now){
    if(depth == K){
        ret.insert(stoi(now));
        return;
    }

    for(int i=0; i<N; ++i){
        if(vst[i]) continue;

        vst[i] = true;
        string nxt = now + to_string(arr[i]);
        dfs(depth+1, nxt);
        vst[i] = false;
    }
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> K;
    for(int i=0; i<N; ++i) cin >> arr[i];

    dfs(0, "");
    cout << ret.size() << "\n";
    return 0;
}
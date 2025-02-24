#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using pii = pair<int, int>;
const int MAX = 1e9+1;
int N;
vector<pii> taste(10);

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> N;
    int sour, bitter;
    for(int i=0; i<N; ++i){
        cin >> sour >> bitter;
        taste[i].first = sour;
        taste[i].second = bitter;
    }

    int ret = MAX;
    int total = 1 << N;

    for(int i=1; i<total; ++i){
        int ts = 1, tb = 0;
        for(int j=0; j<N; ++j){
            if(i & (1 << j)) {
                ts *= taste[j].first;
                tb += taste[j].second;
            }
        }
        ret = min(ret, abs(ts-tb));
    }
    cout << ret << "\n";
    return 0;
}
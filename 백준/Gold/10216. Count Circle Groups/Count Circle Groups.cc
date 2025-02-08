#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;
using pii = pair<int, int>;
using vi = vector<int>;

struct Point{
    int x, y, r;
};

int T, N;
int parent[3001];
Point arr[3001];

int findParent(int me){
    if(parent[me] == me) return me;
    else return parent[me] = findParent(parent[me]);
}

void unionParent(int u, int v){
    int pu = findParent(u);
    int pv = findParent(v);
    if(pu > pv) swap(pu, pv);
    if(pu != pv) parent[pv] = pu;
}

bool checkRange(Point now, Point nxt){
    int xDiff = abs(now.x-nxt.x);
    int yDiff = abs(now.y-nxt.y);

    xDiff *= xDiff;
    yDiff *= yDiff;
    int rSum = (now.r + nxt.r);

    if(xDiff + yDiff <= rSum*rSum) return true;
    else return false;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> T;
    while (T--) {
        cin >> N;
        for(int i=0; i<N; ++i) {
            int x, y, r;
            cin >> x >> y >> r;
            parent[i] = i;
            arr[i].x = x, arr[i].y = y, arr[i].r = r;
        }

        for(int i=0; i<N; ++i){
            for(int j=i+1; j<N; ++j){
                if(findParent(i) != findParent(j)){
                    if(checkRange(arr[i], arr[j])){
                        unionParent(i, j);
                    }
                }
            }
        }
        unordered_set<int> ret;
        for(int i=0; i<N; ++i){
            ret.emplace(findParent(i));
        }
        cout << ret.size() << "\n";
    }
    return 0;
}
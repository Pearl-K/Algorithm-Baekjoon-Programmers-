#include <iostream>
#include <unordered_map>
#include <set>
#include <vector>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

ll H, W, N;
int drdc[9][2] = {{0,0}, {0,-1}, {-1,-1}, {-1,0}, {-1,1}, {0,1}, {1,1}, {1,0}, {1,-1}};
set<pii> grid;
set<pii> checkPoint;
vector<ll> retCnt(10, 0);
ll totalCnt = 0;
ll bitCnt = 0;

void cntBits(pii point, int idx) {
    pii center = {point.first + drdc[idx][0], point.second + drdc[idx][1]};
    if(checkPoint.count(center)) return;
    
    ll tmpCnt = 0;
    for(int i=0; i<9; ++i){
        pii tmpPos = {center.first + drdc[i][0], center.second + drdc[i][1]};
        if(tmpPos.first < 1 || tmpPos.second < 1 || tmpPos.first > H || tmpPos.second > W) return;
        if(grid.count(tmpPos)) tmpCnt++;       
    }
    checkPoint.insert(center);
    retCnt[tmpCnt]++;
    bitCnt++;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> H >> W >> N;
    for(int i=0; i<N; ++i){
        int r, c;
        cin >> r >> c;
        grid.insert({r, c});
    }
    
    for(auto point: grid){
        for(int i=0; i<9; ++i){
            cntBits(point, i);
        }
    }
    
    totalCnt = (W-2)*(H-2) - bitCnt;
    retCnt[0] = totalCnt;
    for(int i=0; i<10; ++i) cout << retCnt[i] << "\n";
    return 0;
}
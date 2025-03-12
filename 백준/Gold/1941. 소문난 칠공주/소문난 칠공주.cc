#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using pii = pair<int, int>;
int pos[5][5];
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

bool checkAdj(int bit){
    vector<pii> pos;
    for(int i=0; i<25; ++i){
        if(bit & (1<<i)) {
            int r=i/5;
            int c=i%5;
            pos.push_back({r,c});
        }
    }
    
    int cnt = 1;
    queue<pii> q;
    bool vst[5][5] = {false, };
    q.push(pos[0]);
    vst[pos[0].first][pos[0].second] = true;

    while(!q.empty()){
        pii now = q.front();
        q.pop();

        int r=now.first;
        int c=now.second;

        for(int i=0; i<4; ++i){
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr >=0 && nr < 5 && nc >=0 && nc<5 && !vst[nr][nc]) {
                if (bit & (1 << (nr * 5 + nc))) {
                    vst[nr][nc] = true;
                    q.emplace(nr, nc);
                    cnt++;
                }
            }
        }
    }
    return (cnt==7);
}

bool checkDPower(int bit){
    int power=0;
    for(int i=0; i<25; ++i){
        if(bit &(1<<i)){
            int r=i/5;
            int c=i%5;
            if(pos[r][c]==1) power++;
        }
    }
    return (power>=4);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    for(int i=0; i<5; ++i){
        for(int j=0; j<5; ++j){
            char c;
            cin >> c;
            pos[i][j] = (c=='S') ? 1 : 0;
        }
    }
    int ret = 0;
    for(int bit=0; bit<(1<<25); ++bit){
        if(__builtin_popcount(bit)==7){
            if(checkDPower(bit) && checkAdj(bit)) ret++;
        }
    }
    cout << ret << "\n";
    return 0;
}
#include <iostream>
#include <queue>
#include <cstring>
#include <vector>
using namespace std;
using pii = pair<int, int>;
using vi = vector<int>;

struct marble {
    int rr, rc, br, bc, cnt;
};

marble start;
int N, M;
int grid[12][12];
bool vst[11][11][11][11] = {false, };
const int MAX_CNT = 10;
const int dr[4] = {-1, 1, 0, 0};
const int dc[4] = {0, 0, -1, 1};

int bfs() {
    queue<marble> q;
    q.push(start);
    vst[start.rr][start.rc][start.br][start.bc] = true;

    int ret = -1;
    while(!q.empty()) {
        marble cur = q.front();
        q.pop();
        if(cur.cnt > MAX_CNT) break;
        if(grid[cur.rr][cur.rc] == 1 && grid[cur.br][cur.bc] != 1) {
            ret = cur.cnt;
            break;
        }

        for(int i=0; i<4; ++i) {
            int nrr = cur.rr;
            int nrc = cur.rc;
            int nbr = cur.br;
            int nbc = cur.bc;

            // red moves
            while(true) {
                if(grid[nrr][nrc] != -1 && grid[nrr][nrc] != 1) {
                    nrr += dr[i];
                    nrc += dc[i];
                }
                else {
                    if(grid[nrr][nrc] == -1) {
                        nrr -= dr[i];
                        nrc -= dc[i];
                    }
                    break;
                }
            }

            // blue moves
            while(true) {
                if(grid[nbr][nbc] != -1 && grid[nbr][nbc] != 1) {
                    nbr += dr[i];
                    nbc += dc[i];
                }
                else {
                    if(grid[nbr][nbc] == -1) {
                        nbr -= dr[i];
                        nbc -= dc[i];
                    }
                    break;
                }
            }

            // same point
            if (nrr == nbr && nrc == nbc) {
                if(grid[nrr][nrc] != 1) {
                    int redDist = abs(nrr - cur.rr) + abs(nrc - cur.rc);
                    int blueDist = abs(nbr - cur.br) + abs(nbc - cur.bc);
                    if (redDist > blueDist) nrr -= dr[i], nrc -= dc[i];
                    else nbr -= dr[i], nbc -= dc[i];
                }
            }

            if(!vst[nrr][nrc][nbr][nbc]) {
                vst[nrr][nrc][nbr][nbc] = true;
                marble nxt;
                nxt.cnt = cur.cnt+1;
                nxt.rr = nrr, nxt.rc = nrc;
                nxt.br = nbr, nxt.bc = nbc;
                q.push(nxt);
            }
        }
    }
    return ret;
}


int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M;
    memset(grid, -1, sizeof(grid));
    for(int i=1; i<=N; ++i) {
        for(int j=1; j<=M; ++j) {
            char tmp;
            cin >> tmp;
            if(tmp == '#') grid[i][j] = -1;
            else grid[i][j] = 0;
            if(tmp == 'R') start.rr = i, start.rc = j;
            if(tmp == 'B') start.br = i, start.bc = j;
            if(tmp == 'O') grid[i][j] = 1;
        }
    }
    start.cnt = 0;
    cout << bfs();
    return 0;
}
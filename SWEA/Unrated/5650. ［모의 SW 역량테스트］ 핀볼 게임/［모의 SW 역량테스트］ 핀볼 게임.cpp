#include <iostream>
#include <queue>
#include <string.h>
using namespace std;
using pii = pair<int, int>;
const int INF = 1e9;

int T, N;
int grid[102][102];
bool hole1st[5] = {false, };
pii one[5]; // 6~10까지의 웜홀 위치
pii two[5];
pii start; // 시작 정점 저장

// 각 칸에서 4방향 저장
int retCnt = 0;
int dr[4] = {0, 0, 1, -1};
int dc[4] = {1, -1, 0, 0};

void init() {
    // 테케 시작할 때 호출할 모든 초기화
    retCnt = 0;

    for(int i=0; i<5; ++i) {
        hole1st[i] = false;
        one[i] = make_pair(0, 0);
        two[i] = make_pair(0, 0);
    }

    // 가장자리를 5번 벽으로 채워준다 (범위 처리 생략)
    for(int i=0; i<N+2; ++i) {
        for(int j=0; j<N+2; ++j){
            grid[i][j] = 5;
        }
    }

}

int change(int block, int d) {
    switch(block) {
        case 1:
            switch(d) {
                case 0: return 1;
                case 1: return 3;
                case 2: return 0;
                case 3: return 2;
            }
            break;
        case 2:
            switch(d) {
                case 0: return 1;
                case 1: return 2;
                case 2: return 3;
                case 3: return 0;
            }
            break;
        case 3:
            switch(d) {
                case 0: return 2;
                case 1: return 0;
                case 2: return 3;
                case 3: return 1;
            }
            break;
        case 4:
            switch(d) {
                case 0: return 3;
                case 1: return 0;
                case 2: return 1;
                case 3: return 2;
            }
            break;
        case 5:
            switch(d) {
                case 0: return 1;
                case 1: return 0;
                case 2: return 3;
                case 3: return 2;
            }
            break;
    }
    return d;
}

void simulate(int x, int y, int dir) {
    int r = x;
    int c = y;
    int d = dir;
    int score = 0;

    while (true) {
        int nr = r + dr[d];
        int nc = c + dc[d];

        // 1. 블랙홀에 도착한 경우
        if (grid[nr][nc] == -1) {
            retCnt = max(retCnt, score);
            break;
        }
            // 2. 시작점 재방문
        else if (nr == start.first && nc == start.second) {
            retCnt = max(retCnt, score);
            break;
        }
            // 3. 웜홀에 도착한 경우
        else if (grid[nr][nc] >= 6) {
            int val = grid[nr][nc] - 6;

            // 웜홀 간 이동(진행 방향 유지)
            if (one[val].first == nr && one[val].second == nc) {
                nr = two[val].first;
                nc = two[val].second;
            }
            else if (two[val].first == nr && two[val].second == nc) {
                nr = one[val].first;
                nc = one[val].second;
            }

            // 좌표가 갱신되었으므로, 바로 다시 방향 이동을 적용
            r = nr;
            c = nc;
            continue;  // 갱신된 좌표로 다시 시뮬레이션
        }
            // 4. 1~5번 블록을 만났을 때
        else if (grid[nr][nc] >= 1 && grid[nr][nc] <= 5) {
            score++; // 충돌 시 점수 증가

            int val = grid[nr][nc];
            d = change(val, d);  // 방향 전환
        }

        // 좌표 업데이트
        r = nr;
        c = nc;
    }
}


int main(void) {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);

    cin >> T;
    for(int t=1; t<=T; ++t) {
        cin >> N;
        init();

        for(int i=1; i<=N; ++i) {
            for(int j=1; j<=N; ++j) {
                cin >> grid[i][j];

                if(grid[i][j] >= 6) {
                    int pos = grid[i][j]-6;

                    //웜홀이 처음 나왔을 때 위치 입력
                    if (!hole1st[pos]) {
                        one[pos] = make_pair(i, j);
                        hole1st[pos] = true;
                    }
                    else { //웜홀이 두 번째 나왔을 때
                        two[pos] = make_pair(i, j);
                    }
                }
            }
        }

        // 각 정점에서 0인 칸에 4방향 출발
        for(int i=1; i<=N; ++i) {
            for(int j=1; j<=N; ++j) {
                if(grid[i][j] == 0) {
                    start = make_pair(i, j); // 시작 좌표 저장
                    for(int d = 0; d < 4; ++d) {
                        simulate(i, j, d);
                    }
                }
            }
        }

        cout << "#" << t << " " << retCnt << "\n";
    }
    return 0;
}

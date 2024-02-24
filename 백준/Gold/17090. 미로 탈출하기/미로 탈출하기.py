import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #10**5 에서는 재귀 터짐 10**6이 안전한듯?
N, M = map(int, input().split())
grid = [list(input().rstrip()) for i in range(N)]

# 경로 겹치는 곳은 모두 탈출 가능, vst 방문이면서 탈출 불가능한 곳은 사이클
vst = [[False for _ in range(M)] for _ in range(N)]
escape = [[False for _ in range(M)] for _ in range(N)]
res, cnt = 0, 0
track = []

def path_track():
    while track: #여기서 기록을 다 비우고 있음
        r, c = track.pop()
        escape[r][c] = True

# 사이클 판별 어떻게?
def dfs(r, c):
    global cnt, res, track

    if 0 <= r < N and 0 <= c < M:
        if vst[r][c] and not escape[r][c]:
            cnt = 0
            track = []
            return
        elif vst[r][c] and escape[r][c]: #탈출가능한 곳에 방문했을 때
            res += cnt
            cnt = 0
            path_track()
            return
        elif not vst[r][c]:
            vst[r][c] = True
            track.append((r, c))
            cnt += 1

            if grid[r][c] == 'U':
                dfs(r-1, c)
            elif grid[r][c] == 'R':
                dfs(r, c+1)
            elif grid[r][c] == 'D':
                dfs(r+1, c)
            else: #L
                dfs(r, c-1)
    else:
        res += cnt
        cnt = 0
        path_track()
        return

for i in range(N):
    for j in range(M):
        if vst[i][j]:
            continue
        else:
            dfs(i, j)
print(res)
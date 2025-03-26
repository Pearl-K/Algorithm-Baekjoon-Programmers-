import sys
input = sys.stdin.readline
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
vst = [[False]*N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
group = 1
INF = sys.maxsize

from collections import deque

def grouping(r, c, g):
    q = deque([])
    q.append((r, c))

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<=nr<N and 0<=nc<N and not vst[nr][nc] and grid[nr][nc]==1:
                vst[nr][nc] = True
                grid[nr][nc] = g
                q.append((nr, nc))

def bfs(g):
    q = deque([])
    dist = [[-1]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == g:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<=nr<N and 0<=nc<N:
                if grid[nr][nc] and grid[nr][nc] != g:
                    return dist[r][c]
                elif grid[nr][nc]==0 and dist[nr][nc]==-1:
                    dist[nr][nc] = dist[r][c]+1
                    q.append((nr, nc))
    return INF

for i in range(N):
    for j in range(N):
        if grid[i][j] and not vst[i][j]:
            vst[i][j] = True
            grid[i][j] = group
            grouping(i, j, group)
            group += 1

res = INF
for i in range(1, group):
    res = min(res, bfs(i))
print(res)
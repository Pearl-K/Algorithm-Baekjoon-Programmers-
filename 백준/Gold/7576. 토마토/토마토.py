from collections import deque
import sys
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for i in range(N)]
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q. append((i, j))

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    q.append((nx, ny))
res = 0
bfs()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit()
    res = max(res, max(i))
print(res-1)
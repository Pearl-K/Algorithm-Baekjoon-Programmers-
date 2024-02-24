import sys
input = sys.stdin.readline

M, N = map(int, input().split())
grid = []
vst = [[-1]*M for _ in range(N)]

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    Q = deque()
    vst[x][y] = 0
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and vst[nx][ny] == -1:
                if grid[nx][ny] == '0':
                    vst[nx][ny] = vst[x][y]
                    Q.appendleft((nx, ny))
                else:
                    vst[nx][ny] = vst[x][y]+1
                    Q.append((nx, ny))

    print(vst[N-1][M-1])

for _ in range(N):
    grid.append(list(input().rstrip()))
bfs(0, 0)

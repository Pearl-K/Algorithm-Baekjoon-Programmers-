import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

#벽 부수고 이동하기 1 문제 살짝 변형
grid = []
path = [[[0]*(K+1) for i in range(M)] for j in range(N)]

from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = sys.maxsize

def BFS(u, v):
    Q = deque()
    Q.append((u, v, K))
    path[u][v][K] = 1

    while Q:
        x, y, cnt = Q.popleft()

        if x == N-1 and y == M-1:
            return path[x][y][cnt]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 1 and cnt > 0 and path[nx][ny][cnt-1] == 0:
                    path[nx][ny][cnt-1] = path[x][y][cnt] + 1
                    Q.append((nx, ny, cnt-1))
                elif grid[nx][ny] == 0 and path[nx][ny][cnt] == 0:
                    path[nx][ny][cnt] = path[x][y][cnt] + 1
                    Q.append((nx, ny, cnt))

    return -1

for i in range(N):
    grid.append(list(map(int, input().rstrip())))
print(BFS(0, 0))
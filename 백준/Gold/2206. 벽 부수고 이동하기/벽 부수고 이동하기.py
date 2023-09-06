import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 1. 벽이 있는 상태로 최단 거리 찾기
# 2. 각각의 벽을 기준으로 (1,1) - 벽 - (N,N) 까지의 최단 경로를 구한 후 min 값 찾기
# 그러나 위 방법은 시간 복잡도 초과, 벽을 모두 스캔하는 브루트포스 외에 최적화가 불가능할까?
# BFS 상에서 벽을 부순 경우와 아닌 경우를 나눠서 관리하는 아이디어?

grid = []
path = [[[0, 0] for i in range(M)] for j in range(N)]

from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = sys.maxsize

def BFS(u, v):
    cnt = 0
    Q = deque()
    Q.append((u, v, cnt))
    path[u][v][0] = 1

    while Q:
        x, y, cnt = Q.popleft()

        if x == N-1 and y == M-1:
            return path[x][y][cnt]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 1 and cnt == 0:
                    path[nx][ny][1] = path[x][y][0] + 1
                    Q.append((nx, ny, 1))

                if grid[nx][ny] == 0 and path[nx][ny][cnt] == 0:
                    path[nx][ny][cnt] = path[x][y][cnt] + 1
                    Q.append((nx, ny, cnt))

    return -1

for i in range(N):
    grid.append(list(map(int, input().rstrip())))
print(BFS(0, 0))
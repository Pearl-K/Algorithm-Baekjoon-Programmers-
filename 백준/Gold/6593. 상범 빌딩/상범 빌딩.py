import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

from collections import deque
def BFS_3D(z, x, y):
    cnt = 0
    visited = [[[False]*C for _ in range(R)] for _ in range(L)]
    Q = deque()
    Q.append((z, x, y, cnt))
    visited[z][x][y] = True

    while Q:
        z, x, y, cnt = Q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and not visited[nz][nx][ny] and grid[nz][nx][ny] != "#":
                visited[nz][nx][ny] = True
                new_cnt = cnt + 1
                if grid[nz][nx][ny] == 'E':
                    return new_cnt
                Q.append((nz, nx, ny, new_cnt))

    return -1

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        sys.exit()

    grid = [[[]*C for _ in range(R)] for _ in range(L)]

    for i in range(L):
        grid[i] = [list(map(str, input().rstrip())) for _ in range(R)]
        input() #blank 처리

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if grid[i][j][k] == 'S':
                    res = BFS_3D(i, j, k)

    if res == -1:
        print("Trapped!")
    else:
        print("Escaped in " + str(res) + " minute(s).")
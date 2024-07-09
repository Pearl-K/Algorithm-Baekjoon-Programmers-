import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
grid = []

for i in range(N):
    grid.append(list(map(int, input().split())))

# 북 동 남 서 (순서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y = r, c
grid[x][y] = 2
cnt = 1

while True:
    is_cleaned = 0
    for _ in range(4):
        d = (d+3)%4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
            grid[nx][ny] = 2
            is_cleaned = 1
            cnt += 1
            x, y= nx, ny
            break

    if not is_cleaned:
        if grid[x-dx[d]][y-dy[d]] == 1:
            print(cnt)
            break
        else:
            x, y = x-dx[d], y-dy[d]

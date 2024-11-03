import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
grid = []

for i in range(N):
    grid.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, limit):
    vst[r][c] = True

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not vst[nr][nc] and grid[nr][nc] > limit:
            dfs(nr, nc, limit)

    return 1

res = 0
for h in range(101):
    vst = [[False for i in range(N)] for _ in range(N)]
    tmp = 0

    for i in range(N):
        for j in range(N):
            if not vst[i][j] and grid[i][j] > h:
                tmp += dfs(i, j, h)

    res = max(res, tmp)
print(res)
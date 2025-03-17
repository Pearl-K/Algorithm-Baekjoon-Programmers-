import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
res = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    arr[x][y] = 0 #like visited
    w = 1
    q = []
    q.append([x, y])
    
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                q.append([nx, ny])
                arr[nx][ny] = 0
                w += 1
    return w

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt += 1
            res = max(dfs(i, j), res)

print(cnt)
print(res)
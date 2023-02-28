import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if plant[nx][ny] == 1:
                plant[nx][ny] = 0
                dfs(nx, ny)

T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())
    plant = [[0]*M for i in range(N)]
    cnt = 0

    for j in range(K):
        y, x = map(int, input().split())
        plant[x][y] = 1

    for a in range(N):
        for b in range(M):
            if plant[a][b] == 1:
                dfs(a, b)
                cnt += 1
    print(cnt)


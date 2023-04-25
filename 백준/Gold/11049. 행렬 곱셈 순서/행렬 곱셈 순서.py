import sys
input = sys.stdin.readline
INF = 2**31
N = int(input())
p = []

for i in range(N):
    r, c = map(int, input().split())
    p.append((r, c))

dp = [[0]*(N+1) for i in range(N+1)]

for i in range(1, N+1):
    for j in range(N-i):
        if i == 1:
            dp[j][j+1] = p[j][0]*p[j][1]*p[j+1][1]
        else:
            dp[j][j+i] = INF

            for k in range(j, j+i):
                dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + p[j][0]*p[k][1]*p[j+i][1])
print(dp[0][N-1])

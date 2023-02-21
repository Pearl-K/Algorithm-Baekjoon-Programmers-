import sys
N, K = map(int, sys.stdin.readline().split())
dp = [[1 for j in range(i)] for i in range(1, 31)]
for i in range(2, 30):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp[N-1][K-1])
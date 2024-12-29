import sys
input = sys.stdin.readline
MOD = 1_000_000_003
N = int(input())
K = int(input())
dp = [[0]*1001 for _ in range(1001)]

if N//K < 2:
    print(0)
else:
    for i in range(N+1):
        dp[i][1] = i
        dp[i][0] = 1

    for i in range(2, N+1):
        for j in range(2, K+1):
            dp[i][j] = (dp[i-2][j-1] + dp[i-1][j])%MOD

    res = (dp[N-1][K] + dp[N-3][K-1])%MOD
    print(res)
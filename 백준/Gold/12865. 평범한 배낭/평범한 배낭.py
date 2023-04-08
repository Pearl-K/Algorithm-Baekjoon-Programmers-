import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0 for i in range(K+1)]for j in range(N+1)]
weight = [0 for i in range(N+1)]
value = [0 for i in range(N+1)]

for i in range(1, N+1):
    weight[i], value[i] = map(int, input().split())

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j-weight[i]] + value[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
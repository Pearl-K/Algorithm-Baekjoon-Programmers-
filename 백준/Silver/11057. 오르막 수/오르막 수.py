import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*10 for _ in range(N+1)]
MOD = 10007

for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= MOD

res = 0
for i in range(10):
    res += dp[N][i]
    res %= MOD
#print(dp)
print(res)
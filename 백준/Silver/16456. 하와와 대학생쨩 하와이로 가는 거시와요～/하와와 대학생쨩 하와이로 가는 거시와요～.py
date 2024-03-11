import sys
input = sys.stdin.readline
N = int(input())
MOD = 1_000_000_009

# 2 -1 2 는 한칸의 이동..
dp = [0 for _ in range(50001)]
dp[1] = 1
dp[2] = 1
dp[3] = 2

if N > 3:
    for i in range(4, N+1):
        dp[i] = (dp[i-3]+dp[i-1])%MOD
print(dp[N])
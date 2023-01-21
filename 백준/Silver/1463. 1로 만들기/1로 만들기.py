n = int(input())

dp = [0 for i in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # dp[x]는 횟수, x는 그 때 판단하는 수!

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
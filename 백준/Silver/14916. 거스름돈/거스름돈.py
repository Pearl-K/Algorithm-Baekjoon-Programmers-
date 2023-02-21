n = int(input())
dp = [-1, -1, 1, -1, 2, 1, 3, 2, 4]
for i in range(9, n+1):
    dp.append(min(dp[i-2], dp[i-5]) + 1)
print(dp[n])
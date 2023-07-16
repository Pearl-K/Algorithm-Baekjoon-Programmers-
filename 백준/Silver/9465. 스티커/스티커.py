import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    dp = []

    for j in range(2):
        dp.append(list(map(int, input().split())))

    if len(dp[0]) == 1:
        print(max(dp[0][0], dp[1][0]))
    else:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for k in range(2, N):
            dp[0][k] += max(dp[1][k-1], dp[1][k-2])
            dp[1][k] += max(dp[0][k-1], dp[0][k-2])

        print(max(dp[0][-1], dp[1][-1]))
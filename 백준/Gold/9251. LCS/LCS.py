def LCS(st1, st2, N, M):
    dp = [[0 for x in range(M+1)] for y in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            if st1[i-1] == st2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

s1 = input()
s2 = input()

print(LCS(s1, s2, len(s1), len(s2)))
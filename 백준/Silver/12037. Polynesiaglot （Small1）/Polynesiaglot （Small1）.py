import sys
T = int(sys.stdin.readline())
for i in range(T):
    C, V, L = map(int, sys.stdin.readline().split())
    dp = [[0, 0]for i in range(L)]
    dp[0][0] = V
    dp[0][1] = 0

    for j in range(1, L):
        dp[j][0] = ((dp[j-1][0] + dp[j-1][1])*V) % (10**9 + 7)
        dp[j][1] = (dp[j-1][0] * C) % (10**9 + 7)
    print("Case #"+str(i+1)+": ", end='')
    print((dp[L-1][0] + dp[L-1][1]) % (10**9 + 7))
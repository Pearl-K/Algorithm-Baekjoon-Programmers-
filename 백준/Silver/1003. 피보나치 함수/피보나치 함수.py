T = int(input())

for i in range(T):
    dp = [[1, 0], [0, 1]]
    test = int(input())
    if test == 0:
        print(*dp[0])
    elif test == 1:
        print(*dp[1])
    else: #test가 2 이상, 40 이하인 자연수일 경우
        for j in range(2, test+1):
            dp.append([dp[j-2][0] + dp[j-1][0], dp[j-2][1] + dp[j-1][1]] )
        print(*dp[test])
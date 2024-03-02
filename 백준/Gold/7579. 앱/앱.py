import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = sum(cost)
dp = [[0 for _ in range(sum(cost)+1)] for _ in range(n+1)]

for i in range(n):
    n_b = arr[i]
    n_c = cost[i]

    for j in range(sum(cost)):
        if j < n_c:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(n_b + dp[i][j-n_c], dp[i][j])

        if dp[i+1][j] >= m:
            res = min(res, j)
print(res if res != 0 else 0)
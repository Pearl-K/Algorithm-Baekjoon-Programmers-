import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    li = list(input().rstrip())
    arr.append(li)

dp = [[0]*M for _ in range(N)]

# 자기 대각선 위 dp[i-1][j-1] 이 정사각형이고,
# 자기까지의 각 row, column이 1이면 ok
# 뭔가 dp[i][j]를 정사각형의 아래 꼭짓점으로 두고 check할 방법?

for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            dp[i][j] = 1

for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            continue
        if min(dp[i][j], dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) != 0:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

res = 0
for i in range(N):
    for j in range(M):
        res = max(res, dp[i][j])
print(res**2)


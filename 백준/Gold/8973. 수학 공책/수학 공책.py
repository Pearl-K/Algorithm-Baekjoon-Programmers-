import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
note = []
for i in range(2):
    note.append(list(map(int, input().split())))

INF = sys.maxsize
now = -INF
ans = (0, 0)
dp = [[-1 for _ in range(2001)] for _ in range(2001)]

def make_dp(left, right):
    if left + right >= N:
        return 0
    if dp[left][right] != -1:
        return dp[left][right]

    res = make_dp(left+ 1, right+ 1)

    if left == N-1-right:
        res += note[0][left] * note[1][left]
    else:
        res += note[0][left] * note[1][N-1-right] + note[0][N-1-right] * note[1][left]

    dp[left][right] = res
    return res

for i in range(N):
    for j in range(N - i):
        result = make_dp(i, j)
        if now < result:
            now = result
            answer = (i, j)

print(*answer, end=' ')
print()
print(now)
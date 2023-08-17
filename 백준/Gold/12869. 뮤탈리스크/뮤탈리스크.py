import sys
input = sys.stdin.readline
INF = sys.maxsize
sys.setrecursionlimit(10**6)

N = int(input())
SCV = list(map(int, input().split()))

while len(SCV) < 3:
    SCV.append(0)

dp = [[[0 for i in range(61)] for j in range(61)] for k in range(61)]

def dfs(x, y, z):
    if x == 0 and y ==0 and z == 0:
        return 0
    if dp[x][y][z]:
        return dp[x][y][z]

    dp[x][y][z] = 1 + min(dfs(max(x - 9, 0), max(y - 3, 0), max(z - 1, 0)),
                          dfs(max(x - 9, 0), max(y - 1, 0), max(z - 3, 0)),
                          dfs(max(x - 3, 0), max(y - 9, 0), max(z - 1, 0)),
                          dfs(max(x - 3, 0), max(y - 1, 0), max(z - 9, 0)),
                          dfs(max(x - 1, 0), max(y - 3, 0), max(z - 9, 0)),
                          dfs(max(x - 1, 0), max(y - 9, 0), max(z - 3, 0)))
    return dp[x][y][z]

print(dfs(SCV[0], SCV[1], SCV[2]))

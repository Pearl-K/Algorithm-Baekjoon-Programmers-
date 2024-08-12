import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
grid = []

for _ in range(N):
    grid.append(list(input().rstrip()))

def cal_min(nowC):
    add = 0
    pre_s = [[0] * (M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if (i+j)%2 == 0:
                if(grid[i][j] != nowC): add = 1
                else: add = 0
            else:
                if (grid[i][j] == nowC): add = 1
                else: add = 0
            pre_s[i+1][j+1] = pre_s[i][j+1] + pre_s[i+1][j] - pre_s[i][j] + add

    res = 2000*2000+1
    for i in range(1, N-K+2):
        for j in range(1, M-K+2):
            res = min(res, pre_s[i+K-1][j+K-1]-pre_s[i+K-1][j-1]-pre_s[i-1][j+K-1] + pre_s[i-1][j-1])
    return res

print(min(cal_min("B"), cal_min("W")))

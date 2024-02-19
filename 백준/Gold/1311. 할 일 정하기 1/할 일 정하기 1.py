import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
todo = [list(map(int, input().split())) for _ in range(n)]
vst = [-1]*(1<<n)

def dfs(row, now):
    res = INF
    if row == n:
        return 0
    if vst[now] != -1:
        return vst[now]
    for i in range(n):
        if (now & (1 << i)) != 0:
            continue
        res = min(res, dfs(row+1, (now | (1<<i))) + todo[row][i])
    vst[now] = res
    return vst[now]
print(dfs(0, 0))
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
MAX = 100001
prs = [0 for _ in range(MAX)]
dp = [0 for _ in range(MAX)]
tree = [[] for _ in range(MAX)]
arr = [0]

N, M = map(int, input().split())
arr += list(map(int, input().split()))

for i in range(1, N+1):
    if arr[i] != -1:
        tree[arr[i]].append(i)

for i in range(M):
    a, b = map(int, input().split())
    dp[a] += b

def dfs(now):
    for nxt in tree[now]:
        if prs[now] == nxt:
            continue
        dp[nxt] += dp[now]
        dfs(nxt)
    
dfs(1)
for i in range(1, N+1):
    print(dp[i], end=" ")
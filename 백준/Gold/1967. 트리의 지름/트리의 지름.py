import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for i in range(n+1)]
dist = [-1]*(n+1)

for i in range(n-1):
    a, b, w = map(int, input().split())
    tree[a].append([b, w])
    tree[b].append([a, w])

def dfs(u, w):
    for node in tree[u]:
        now_n, now_w = node
        if dist[now_n] == -1:
            dist[now_n] = now_w + w
            dfs(now_n, dist[now_n])

dist[1] = 0
dfs(1, 0)
first = dist.index(max(dist))
dist = [-1]*(n+1)
dist[first] = 0
dfs(first, 0)

print(max(dist))

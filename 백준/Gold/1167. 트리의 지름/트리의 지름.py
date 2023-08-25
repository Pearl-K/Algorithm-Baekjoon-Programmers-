import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

v = int(input())
tree = [[] for i in range(v+1)]
dist = [-1]*(v+1)

for i in range(v):
    arr = list(map(int, input().split()))
    p = arr[0]
    j = 0
    while True:
        if j >= (len(arr)-2):
            break
        tree[p].append([arr[j+1], arr[j+2]])
        j += 2

def dfs(u, w):
    for node in tree[u]:
        now_n, now_w = node
        if dist[now_n] == -1:
            dist[now_n] = now_w + w
            dfs(now_n, dist[now_n])

dist[1] = 0
dfs(1, 0)
first = dist.index(max(dist))
dist = [-1]*(v+1)
dist[first] = 0
dfs(first, 0)

#print(tree)
print(max(dist))

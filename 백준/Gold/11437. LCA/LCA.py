import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [i for i in range(n+1)]
vst = [False]*(n+1)
depth = [0]*(n+1)

sys.setrecursionlimit(10**5)

def dfs(n, d):
    vst[n] = True
    depth[n] = d

    for node in tree[n]:
        if vst[node]:
            continue
        parent[node] = n
        dfs(node, d+1)

dfs(1, 0)

def lca(x, y):
    while depth[x] != depth[y]:
        if depth[x] > depth[y]:
            x = parent[x]
        else:
            y = parent[y]

    while x != y:
        x = parent[x]
        y = parent[y]

    return x

m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    print(lca(x, y))
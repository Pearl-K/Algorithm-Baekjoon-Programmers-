import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = sys.maxsize
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n+1):
    for j in range(n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
            
parent = [i for i in range(n+1)]

def find(target):
    if target == parent[target]:
        return target
    
    target = find(parent[target])
    return target

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if graph[i][j] >= 1:
            union(i, j)
    
U = list(set(parent))
res = []
for i in range(1, len(U)):
    tmp = INF
    tmpidx = -1
    for j in range(1, n+1):
        if U[i] == parent[j] and tmp > max(graph[j]):
            tmp = max(graph[j])
            tmpidx = j
    res.append(tmpidx)
res.sort()
print(len(res))
for r in res:
    print(r)
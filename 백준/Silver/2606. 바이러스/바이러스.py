import sys
C = int(sys.stdin.readline())
edges = int(sys.stdin.readline())
graph = [[] for i in range(C+1)]
visited= [0 for i in range (C+1)]
for i in range(edges):
    n, v = map(int, sys.stdin.readline().split())
    graph[n] += [v]
    graph[v] += [n]

def dfs(v):
    visited[v] = 1
    for n in graph[v]:
        if visited[n] == 0:
            dfs(n)
dfs(1)
print(sum(visited)-1)
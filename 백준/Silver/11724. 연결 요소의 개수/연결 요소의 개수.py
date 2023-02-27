import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
visited = [0]*(N+1)
cnt = 0
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, start):
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i)

for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i)
        cnt += 1

print(cnt)
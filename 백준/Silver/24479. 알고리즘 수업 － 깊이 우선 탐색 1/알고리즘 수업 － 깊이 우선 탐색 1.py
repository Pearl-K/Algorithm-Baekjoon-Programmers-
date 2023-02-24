import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(N+1)
cnt = 1
def dfs(start_node):
    global cnt
    visited[start_node] = cnt
    graph[start_node].sort()
    
    for i in graph[start_node]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)
dfs(R)

for i in range(1, N+1):
    print(visited[i])
            
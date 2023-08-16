import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
reverse_g = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverse_g[b].append(a)

def dfs(node, visited, stack):
    visited[node] = 1

    for n in graph[node]:
        if visited[n] == 0:
            dfs(n, visited, stack)
    stack.append(node)

def reversed_dfs(node, visited, stack):
    visited[node] = 1
    stack.append(node)

    for n in reverse_g[node]:
        if visited[n] == 0:
            reversed_dfs(n, visited, stack)

visited = [0]*(N+1)
stack = []

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i, visited, stack)

visited = [0]*(N+1)
res = []

while stack:
    SSC = []
    now = stack.pop()
    if visited[now] == 0:
        reversed_dfs(now, visited, SSC)
        res.append(sorted(SSC))

res.sort()
print('Yes' if len(res) == 1 else "No")
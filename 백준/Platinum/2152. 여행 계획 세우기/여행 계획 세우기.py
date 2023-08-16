import sys
input = sys.stdin.readline
INF = sys.maxsize
sys.setrecursionlimit(10**6)

N, M, S, T = map(int, input().split())
graph = [[] for _ in range(N+1)]
reversed_g = [[] for _ in range(N+1)]

def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
    stack.append(x)

def reversed_dfs(x):
    scc[x] = cnt

    if cnt not in depth:
        depth[cnt] = 1
    else:
        depth[cnt] += 1
    for i in reversed_g[x]:
        if scc[i] == -1:
            reversed_dfs(i)


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    reversed_g[b].append(a)

visited = [False]*(N+1)
stack = []

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)

cnt = 0
scc = [-1]*(N+1)
depth = {}

while stack:
    node = stack.pop()
    if scc[node] == -1:
        reversed_dfs(node)
        cnt += 1

scc_adj = [[] for _ in range(cnt)]

for i in range(1, N+1):
    for j in graph[i]:
        if scc[i] != scc[j]:
            scc_adj[scc[i]].append(scc[j])

from collections import deque

if S == T:
    print(depth[scc[T]])
else:
    visited = [0] * cnt
    visited[scc[S]] = depth[scc[S]]
    start = deque()
    start.append(scc[S])

    while start:
        x = start.popleft()
        if x == scc[T]:
            continue
        for i in scc_adj[x]:
            nx = visited[x] + depth[i]
            if visited[i] < nx:
                visited[i] = nx
                start.append(i)
    print(visited[scc[T]])
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start, visited_dfs=[]):
    visited_dfs.append(start)
    graph[start].sort()

    for i in graph[start]:
        if i not in visited_dfs:
            dfs(graph, i, visited_dfs)
    return visited_dfs

def bfs(graph, start):
    not_yet, visited_bfs = [], []
    not_yet.append(start)

    while not_yet:
        node = not_yet[0]
        del not_yet[0]

        if node not in visited_bfs:
            visited_bfs.append(node)
            not_yet.extend(graph[node])

    return visited_bfs

print(*dfs(graph, V))
print(*bfs(graph, V))
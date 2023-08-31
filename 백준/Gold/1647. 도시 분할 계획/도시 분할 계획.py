import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

import heapq
def prim(graph, start_node):
    visited[start_node] = 1
    adj = graph[start_node]
    heapq.heapify(adj)
    total_w = 0
    max_w = 0

    while adj:
        now_w, now = heapq.heappop(adj)
        if visited[now] == 0:
            visited[now] = 1
            max_w = max(max_w, now_w)
            total_w += now_w

            for edge in graph[now]:
                if visited[edge[1]] == 0:
                    heapq.heappush(adj, edge)

    return total_w - max_w

res = prim(graph,1)
print(res)
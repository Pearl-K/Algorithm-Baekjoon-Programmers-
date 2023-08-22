import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq
import collections

n, m = map(int,input().split())
graph = collections.defaultdict(list)
visited = [0]*(n+1)

for i in range(m):
    u, v, z, w = map(int, input().split())
    graph[u].append([z, w, u, v])
    graph[v].append([z, w, v, u])


def prim(graph, start_node):
    visited[start_node] = 1
    adj = graph[start_node]
    heapq.heapify(adj)
    res = []
    total_w = 0

    while adj:
        z, w, u, v = heapq.heappop(adj)
        if visited[v] == 0:
            visited[v] = 1
            res.append(z)
            total_w += w
            for edge in graph[v]:
                if visited[edge[3]] == 0:
                    heapq.heappush(adj, edge)

    return total_w, res

tw, res = prim(graph,1)
res.sort()
min_r = ''

for i in range(1, n+1):
    if visited[i] == 0:
        print(-1)
        sys.exit()

for i in range(len(res)):
    min_r += str(res[i])
print(min_r, tw)
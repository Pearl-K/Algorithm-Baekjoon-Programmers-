import sys
import heapq as hq
input = sys.stdin.readline
inf = sys.maxsize

N, M, K, X = map(int, input().split())
graph = [[] for i in range(N+1)]
dist = [inf]*(N+1)
minheap = []

def dijkistra(graph, dist, start):
    hq.heappush(minheap, [0, start])
    dist[start] = 0

    while minheap:
        u, v = hq.heappop(minheap)

        if dist[v] < u:
            continue
        for new_node, new_dist in graph[v]:
            alt = new_dist + u

            if alt < dist[new_node]:
                dist[new_node] = alt
                hq.heappush(minheap, [alt, new_node])
    return dist

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append([v, 1])

dijkistra(graph, dist, X)
result = []

for i in range(1, N+1):
    if dist[i] == K:
        result.append(i)
if result:
    print(*result, end='\n')
else:
    print(-1)
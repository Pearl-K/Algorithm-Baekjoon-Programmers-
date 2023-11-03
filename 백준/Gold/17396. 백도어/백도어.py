import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
arr = list(map(int, input().strip().split()))
arr[-1] = 0
graph = [[] for _ in range(N)]

for i in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))
    graph[b].append((t, a))

import heapq as hq

def dijkstra(start, end):
    dist = [INF for _ in range(N)]
    dist[start] = 0

    pq = []
    hq.heappush(pq, (0, start))

    while pq:
        d, node = hq.heappop(pq)
        if d > dist[node]:
            continue

        for n_c, n_n in graph[node]:
            if dist[n_n] > dist[node]+n_c and not arr[n_n]:
                dist[n_n] = dist[node]+n_c
                hq.heappush(pq, (dist[n_n], n_n))

    return dist[end]

res = dijkstra(0, N-1)
print(-1 if res == INF else res)
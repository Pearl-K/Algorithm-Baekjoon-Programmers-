import sys
import heapq as hq
input = sys.stdin.readline
sys.setrecursionlimit(10**6+1)
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
ind = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    ind[b] += 1

for i in range(1, N+1):
    graph[i].sort()

heap = []
for i in range(1, N+1):
    if ind[i] == 0:
        hq.heappush(heap, i)

for i in range(N):
    node = hq.heappop(heap)
    print(node, end=" ")
    graph[node].sort()
    
    for nxt in graph[node]:
        ind[nxt] -= 1
        if ind[nxt] == 0:
            hq.heappush(heap, nxt)
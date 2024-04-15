import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indgr = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indgr[b] += 1
#print(graph)
#print(indgr)

for i in range(1, N+1):
    graph[i].sort()

import heapq as hq
H = []
for i in range(1, N+1):
    if indgr[i] == 0:
        hq.heappush(H, i)

for i in range(N):
    now = hq.heappop(H)
    print(now, end =' ')
    graph[now].sort()

    for nxt in graph[now]:
        indgr[nxt] -= 1
        if indgr[nxt] == 0:
            hq.heappush(H, nxt)
import heapq as hq
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
visited = [0]*(N+1)

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

def Prim(start):
    minheap = []
    total_w = 0  # 전체 가중치
    visited[start] = 1

    for i in graph[start]:
        hq.heappush(minheap, i)

    while minheap:
        w, v = hq.heappop(minheap)
        if visited[v] == 0:
            visited[v] = 1
            total_w += w
            for edge in graph[v]:
                if visited[edge[1]] == 0:
                    hq.heappush(minheap, edge)
        if sum(visited) == N:
            return total_w

print(Prim(1))
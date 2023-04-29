import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, R = map(int, input().split()) #M이 수색 범위!
item = list(map(int, input().split()))

graph = [[] for i in range(N+1)]

for i in range(R):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

import heapq as hq

def dijkstra(start):
    Q = []
    #(가중치, 시작 노드) 순서대로 큐에 집어넣기
    hq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        distance, now = hq.heappop(Q)
        if dist[now] < distance:
            continue

        for node, d in graph[now]:
            cost = d + distance
            if cost < dist[node]:
                dist[node] = cost
                hq.heappush(Q, (cost, node))
result = 0
for i in range(1, N+1):
    dist = [INF]*(N+1) #다익스트라 거리 배열 초기화
    dijkstra(i)
    tmp = 0
    for a, b in enumerate(dist):
        if b <= M: #수색 거리 안에 있을 때
            tmp += item[a-1]
    if tmp > result:
        result = tmp
print(result)
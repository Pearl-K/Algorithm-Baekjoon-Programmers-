import sys
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
graph = [[]*(V+1) for i in range(V+1)]

for i in range(E): #그래프 인접리스트 만들기
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

import heapq as hq
INF = sys.maxsize

def dijkstra(graph, start):
    dist = [INF] *(V+1)
    dist[start] = 0 # 시작지점 0으로 시작
    PQ = [] # 우선순위 큐 만들기
    hq.heappush(PQ, (0, start)) #시작 노드와 시작 dist값 넣기
    #거리가 먼저 들어가야 한다.

    while PQ:
        distance, node = hq.heappop(PQ)

        if dist[node] < distance: #기존 거리가 새로운 거리보다 더 작을 때
            continue

        for i in graph[node]:
            alt = i[1] + distance
            if alt < dist[i[0]]:
                dist[i[0]] = alt
                hq.heappush(PQ, (alt, i[0]))
    return dist

res = dijkstra(graph, K)

for i in range(1, V+1):
    if res[i] == INF:
        print('INF')
    else:
        print(res[i])
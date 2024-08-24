import sys
input = sys.stdin.readline
INF = 2000001

import heapq as hq
def dijkstra(start):
    dist = [INF for _ in range(n+1)]
    dist[start] = 0
    pq = []
    hq.heappush(pq, (0, start))

    while pq:
        di, no = hq.heappop(pq)
        if dist[no] < di:
            continue

        for i in graph[no]:
            if dist[i[1]] > i[0] + di:
                dist[i[1]] = i[0] + di
                hq.heappush(pq, (dist[i[1]], i[1]))
    return dist

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))

    cand = [] # 목적지 후보
    for i in range(t):
        cand.append(int(input()))

    s_dijk = dijkstra(s) #출발지로부터 최단거리
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h)

    res = []
    for end in cand:
        # g -> h 경로
        gh = s_dijk[g] + g_dijk[h] + h_dijk[end]
        # h -> g 경로
        hg = s_dijk[h] + h_dijk[g] + g_dijk[end]
        #print(gh, hg)

        if gh == s_dijk[end] or hg == s_dijk[end]:
            res.append(end)
    res.sort()
    print(*res)
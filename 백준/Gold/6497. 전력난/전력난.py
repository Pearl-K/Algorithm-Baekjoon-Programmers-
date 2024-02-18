import sys
import heapq as hq
input = sys.stdin.readline

def find_p(me):
    if par[me] != me:
        par[me] = find_p(par[me])
    return par[me]

def union(u, v):
    u = find_p(u)
    v = find_p(v)
    if u < v: #더 작은 값을 기준으로 union
        par[v] = u
    else:
        par[u] = v

def kruskal():
    res = 0
    while edges:
        cost, x, y = hq.heappop(edges)

        if find_p(x) != find_p(y):
            union(x, y)
            res += cost
    return res

while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break

    edges = []
    cost_s = 0
    par = [i for i in range(M+1)]

    for _ in range(N):
        line = list(map(int, input().split()))
        cost_s += line[2]
        hq.heappush(edges, (line[2], line[0], line[1])) #z 가중치를 기준으로 min heap에 넣기
    print(cost_s-kruskal())

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

    for i in range(len(edges)):
        cost, x, y = edges[i][0], edges[i][1], edges[i][2]
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
        x, y, z = list(map(int, input().split()))
        cost_s += z
        edges.append((z, x, y))
    edges.sort() #그냥 간선 정렬이랑 pq랑 속도 차이가 얼마나 날까...
    print(cost_s-kruskal())
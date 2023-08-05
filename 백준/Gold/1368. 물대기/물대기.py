import sys
input = sys.stdin.readline
N = int(input())
cost = [[]*(N+1) for _ in range(N+1)]
for i in range(N):
    cost[0].append((int(input()), i+1))

temp = []
for _ in range(N):
    temp.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        cost[i+1].append((temp[i][j], j+1))

import heapq as hq
visited = [False]*(N+1)
res = 0

def prim(start):
    global res
    PQ = []
    visited[start] = True
    for node in cost[start]:
        hq.heappush(PQ, node)

    while PQ:
        w, v = hq.heappop(PQ)
        if visited[v] == True:
            continue
        else:
            visited[v] = True
            res += w

        for weight, node in cost[v]:
            if visited[node] == False:
                hq.heappush(PQ, (weight, node))
    return res

print(prim(0))

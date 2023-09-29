import sys
input = sys.stdin.readline

n = int(input())
pnt = []
for _ in range(n):
    a, b = map(float, input().split())
    pnt.append((a, b))

INF = sys.maxsize
dist = [[INF for _ in range(n)] for _ in range(n)]
import math

# 좌표 사이의 dist 값 전처리 O(N**2) >> 10000
for i in range(n):
    for j in range(n):
        if i != j:
            dist[i][j] = math.sqrt((pnt[i][0]-pnt[j][0])**2 + (pnt[i][1] - pnt[j][1])**2)
#print(dist)

import heapq as hq
mst = []
vst = set()
res = 0

def prim():
    global res
    hq.heappush(mst, (0, 0))

    while len(vst) <= n-1:
        now_d, now_n = hq.heappop(mst)
        if now_n in vst:
            continue
        vst.add(now_n)
        res += now_d
        for next in range(n):
            if now_n != next and next not in vst:
                hq.heappush(mst, (dist[now_n][next], next))
prim()
print(res)
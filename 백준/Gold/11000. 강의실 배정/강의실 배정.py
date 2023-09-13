import sys
input = sys.stdin.readline
N = int(input())

import heapq as hq

lec = [list(map(int, input().split())) for _ in range(N)]
lec.sort()
PQ = []
hq.heappush(PQ, lec[0][1])

for i in range(1, N):
    if lec[i][0] < PQ[0]:
        hq.heappush(PQ, lec[i][1])
    else:
        hq.heappop(PQ)
        hq.heappush(PQ, lec[i][1])
print(len(PQ))
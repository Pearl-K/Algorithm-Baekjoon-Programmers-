import sys
input = sys.stdin.readline

N, K = map(int, input().split())
item = []
bag = []

for _ in range(N):
    m, v = map(int, input().split())
    item.append((m, v))

for _ in range(K):
    c = int(input())
    bag.append(c)

bag.sort()

import heapq as hq
H = []
hq.heapify(item)
res = 0

for nw in bag:
    while item and item[0][0] <= nw:
        hq.heappush(H, -item[0][1])
        hq.heappop(item)

    if H:
        res -= hq.heappop(H) #음수 저장이니까 빼주기
print(res)

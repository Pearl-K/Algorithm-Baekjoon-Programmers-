import sys
input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))
d = int(input())

check = []
for node in arr:
    h = node[0]
    o = node[1]
    if abs(o-h) <= d:
        check.append([min(h, o), max(h, o)])

check.sort(key=lambda x:x[1])

import heapq as hq

h = []
res = 0
for node in check:
    if not h:
        hq.heappush(h, node)
    else:
        while h[0][0] < node[1]-d:
            hq.heappop(h)
            if not h:
                break
        hq.heappush(h, node)
    res = max(res, len(h))
print(res)
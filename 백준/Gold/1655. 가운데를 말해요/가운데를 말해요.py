import sys
input = sys.stdin.readline

n = int(input())
left = [] #max heap
right = [] #min heap

import heapq as hq

for i in range(n):
    now = int(input())
    if len(left) == len(right):
        hq.heappush(left, -now)
    else:
        hq.heappush(right, now)

    if right and right[0] < -left[0]:
        left_top = -hq.heappop(left)
        right_top = hq.heappop(right)
        hq.heappush(left, -right_top)
        hq.heappush(right, left_top)

    print(-left[0])
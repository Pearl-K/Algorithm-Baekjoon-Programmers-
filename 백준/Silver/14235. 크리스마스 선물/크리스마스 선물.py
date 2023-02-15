import sys
import heapq
#가치가 큰 선물 -> max heap
n = int(sys.stdin.readline())
max_heap = []
for i in range(n):
    a = input()
    if a == '0':
        if max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(-1)
    else:
        gifts = list(map(int,a.split()))
        for j in gifts[1:]:
            heapq.heappush(max_heap, -j)
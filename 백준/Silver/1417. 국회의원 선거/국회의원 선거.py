import sys
import heapq
N = int(sys.stdin.readline())
max_heap = []
for i in range(N):
    a = int(sys.stdin.readline())
    if i == 0:
        one = a
    else:
        heapq.heappush(max_heap, a * (-1))

if N == 1:
    print(0)
else:
    cnt = 0
    while max_heap:
        a = -heapq.heappop(max_heap)
        if one > a:
            break
        one += 1
        cnt += 1
        heapq.heappush(max_heap, (-1)*(a-1))
    print(cnt)
import heapq
import sys
N = int(sys.stdin.readline())
min_heap = []
for i in range(N):
  a = int(sys.stdin.readline())
  if a == 0:
    if min_heap:
      print(heapq.heappop(min_heap))
    else:
      print(0)
  else:
    heapq.heappush(min_heap, a)
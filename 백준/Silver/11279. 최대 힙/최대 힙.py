import heapq
import sys

N = int(sys.stdin.readline())
max_heap = []
for i in range(N):
  a = int(sys.stdin.readline())
  if a == 0:
    if max_heap:
      print(heapq.heappop(max_heap)*(-1))
    else:
      print(0)
  else:
    heapq.heappush(max_heap, a*(-1))
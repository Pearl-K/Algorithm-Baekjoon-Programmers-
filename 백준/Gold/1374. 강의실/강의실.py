import heapq
import sys

N = int(sys.stdin.readline())
class_list = []
  
for i in range(N):
  num, start, end = map(int, sys.stdin.readline().split())
  class_list.append([num, start, end])
class_list.sort(key=lambda x:x[1])

min_heap = []
cnt = 0

for i in class_list:
  while min_heap and min_heap[0] <= i[1]:
    heapq.heappop(min_heap)
  heapq.heappush(min_heap, i[2]) #수업 끝나는 시간 추가
  cnt = max(cnt, len(min_heap))

print(cnt)
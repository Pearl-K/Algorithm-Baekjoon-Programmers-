import sys
import heapq
N, M = map(int, sys.stdin.readline().split())
gifts = []
for i in list(map(int, sys.stdin.readline().split())):
    heapq.heappush(gifts, -i)
kids = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    if kids[i] <= -gifts[0]:
        a = -heapq.heappop(gifts)
        heapq.heappush(gifts, -(a-kids[i]))
    else:
        print(0)
        sys.exit()
print(1)
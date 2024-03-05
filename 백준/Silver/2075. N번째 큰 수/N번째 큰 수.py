import sys
input = sys.stdin.readline

import heapq as hq
H = []
N = int(input())
for _ in range(N):
    li = list(map(int, input().split()))

    for i in range(N):
        if len(H) < N:
            hq.heappush(H, li[i])
        elif len(H) == N:
            now = hq.heappop(H)

            if li[i] > now:
                hq.heappush(H, li[i])
            else:
                hq.heappush(H, now)

res = hq.heappop(H)
print(res)
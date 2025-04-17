import sys
input = sys.stdin.readline
from collections import deque

N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
res, cnt = 0, 0
eat = deque([])

for i in range(k-1):
    eat.append(arr[i])

for j in range(N):
    eat.append(arr[(j+k-1)%N])
    cnt = 0
    if c not in eat:
        cnt = 1
    res = max(res, len(set(eat))+cnt)
    eat.popleft()
print(res)
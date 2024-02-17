import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

import math
std = int(math.ceil(9*M/10)) #이 개수 이상의 같은 값 존재

from collections import deque
l, r = 0, M-1
Q = deque()
cnt = [0]*(10**6+1)

for i in range(0, M):
    now = arr[i]
    Q.append(now)
    cnt[now] += 1

    if cnt[now] >= std:
        print('YES')
        sys.exit()


for r in range(M, N):
    now = Q.popleft()
    cnt[now] -= 1

    new = arr[r]
    Q.append(new)
    cnt[new] += 1
    
    if cnt[new] >= std:
        print('YES')
        sys.exit()
print('NO')
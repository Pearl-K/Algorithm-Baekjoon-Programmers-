import sys
input = sys.stdin.readline
N, K = map(int, input().split())
MAX = 100001
vst = [0 for _ in range(MAX)]
res = 0
cnt = 0

from collections import deque
Q = deque([])
Q.append(N)

while Q:
    now = Q.popleft()
    tmp = vst[now]
    if now == K:
        res = tmp
        cnt += 1
        continue
    for nxt in [now-1, now+1, now*2]:
        if 0 <= nxt < MAX and (vst[nxt] == 0 or vst[nxt] == vst[now]+1):
            vst[nxt] = vst[now]+1
            Q.append(nxt) 
print(res)
print(cnt)
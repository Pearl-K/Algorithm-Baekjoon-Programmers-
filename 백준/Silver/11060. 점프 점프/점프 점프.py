import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
def bfs():
    q = deque()
    q.append((0, 0))
    vst = [False]*N
    vst[0] = True
    while q:
        pos, cnt = q.popleft()
        if pos == N-1:
            return cnt
        for i in range(1, arr[pos] + 1):
            nxt = pos+i
            if nxt >= N:
                break
            if not vst[nxt]:
                vst[nxt] = True
                q.append((nxt, cnt+1))
    return -1
print(bfs())
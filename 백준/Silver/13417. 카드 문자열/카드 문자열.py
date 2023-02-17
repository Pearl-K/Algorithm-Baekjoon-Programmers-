import sys
from collections import deque
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    st = list(sys.stdin.readline().split())
    dq = deque(st)
    res = deque()
    for j in range(N):
        if j == 0:
            res.append(dq.popleft())
        else:
            if dq:
                if ord(dq[0]) <= ord(res[0]):
                    res.appendleft(dq.popleft())
                else:
                    res.append(dq.popleft())
    print(''.join(res))
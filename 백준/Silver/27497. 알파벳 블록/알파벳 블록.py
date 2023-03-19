import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()
cnt = []

for i in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == '1':
        dq.append(command[1])
        cnt.append(1)
    elif command[0] == '2':
        dq.appendleft(command[1])
        cnt.append(2)
    else:
        if dq:
            a = cnt.pop()
            if a == 1:
                dq.pop()
            elif a == 2:
                dq.popleft()

if dq:
    print(''.join(dq))
else:
    print(0)
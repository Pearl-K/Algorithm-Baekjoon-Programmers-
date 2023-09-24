import sys
input = sys.stdin.readline

from collections import deque
N = int(input())
Q = deque(enumerate(map(int, input().split())))
res = []

while Q:
    i, p = Q.popleft()
    res.append(i+1)
    if p > 0:
        Q.rotate(-(p - 1))
    elif p < 0:
        Q.rotate(-p)
print(*res)
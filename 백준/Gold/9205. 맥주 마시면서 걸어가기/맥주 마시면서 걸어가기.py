import sys
input = sys.stdin.readline

from collections import deque
T = int(input())

def bfs():
    Q = deque()
    Q.append((sx, sy))

    while Q:
        x, y = Q.popleft()
        if abs(x-fx) + abs(y-fy) <= 1000:
            print("happy")
            return

        for i in range(N):
            if not vst[i]:
                nx, ny = market[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    Q.append((nx, ny))
                    vst[i] = True
    print("sad")


for _ in range(T):
    N = int(input())
    sx, sy = map(int, input().split())
    market = []
    for i in range(N):
        mx, my = map(int, input().split())
        market.append((mx, my))

    fx, fy = map(int, input().split())
    vst = [False]*(N+1)
    bfs()
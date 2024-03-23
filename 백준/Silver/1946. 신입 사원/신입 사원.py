import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    sc = []
    for i in range(N):
        a, b = map(int, input().split())
        sc.append((a, b))

    sc.sort()
    cnt, cur = 1, 0

    for i in range(1, N):
        if sc[i][1] < sc[cur][1]:
            cur = i
            cnt += 1
    print(cnt)

import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    M, N, X, Y = map(int, input().split())
    res = -1

    tmp = X
    while tmp <= M*N:
        if (tmp-X) % M == 0 and (tmp-Y) % N == 0:
            res = tmp
            break
        tmp += M
    print(res)
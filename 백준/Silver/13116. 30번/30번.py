import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    a, b = map(int, input().split())

    while True:
        if a == b:
            print(a*10)
            break
        if a > b:
            a //= 2
        else:
            b //= 2
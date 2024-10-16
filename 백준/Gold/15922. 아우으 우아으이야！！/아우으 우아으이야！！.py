import sys
input = sys.stdin.readline
N = int(input())
start, end = map(int, input().split())
res = 0

for i in range(N-1):
    x, y = map(int, input().split())

    if x <= end:
        if y > end:
            end = y
    else:
        res += (end-start)
        start = x
        end = y
res += (end-start)
print(res)

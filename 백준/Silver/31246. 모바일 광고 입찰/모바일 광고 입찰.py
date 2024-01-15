import sys
input = sys.stdin.readline
n, k = map(int, input().split())
cnt = 0
cost_diff = []

for i in range(n):
    a, b = map(int, input().split())
    if a >= b:
        cnt += 1
    else:
        cost_diff.append(b-a)

if cnt >= k:
    print(0)
else:
    cost_diff.sort()
    for i in range(len(cost_diff)):
        if cnt + (i+1) >= k:
            print(cost_diff[i])
            break
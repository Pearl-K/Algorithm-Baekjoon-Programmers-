import sys
input = sys.stdin.readline

prime = []
arr = [0] * 1000001
arr[0] = 1
arr[1] = 1

for i in range(2, 1000001):
    if arr[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            arr[j] = 1

t = int(input())

for i in range(t):
    cnt = 0
    n = int(input())
    for p in prime:
        if p >= n:
            break
        if not arr[n-p] and p <= n-p:
            cnt += 1
    print(cnt)
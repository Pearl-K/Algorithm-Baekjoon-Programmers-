import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    odd = []
    even = []
    res = [0] * N

    for i in range(N):
        if arr[i] % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort(reverse=True)

    for i in range(N):
        if arr[i] % 2 == 0:
            res[i] = even.pop()
        else:
            res[i] = odd.pop()
    print("Case #" + str(t+1) + ":", *res)

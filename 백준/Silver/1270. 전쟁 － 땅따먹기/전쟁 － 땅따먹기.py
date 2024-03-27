import sys
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    dic = dict()
    arr = list(map(int, input().split()))
    T = arr[0]

    val = 0
    key = 0

    for i in range(1, len(arr)):
        now = arr[i]
        if now not in dic:
            dic[now] = 1
        else:
            dic[now] += 1

        if dic[now] > val:
            val = dic[now]
            key = now

    if val > T/2:
        print(key)
    else:
        print('SYJKGW')
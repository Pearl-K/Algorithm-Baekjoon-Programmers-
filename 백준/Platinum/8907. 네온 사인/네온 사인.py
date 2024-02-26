import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    cnt = [0]*N

    for i in range(N-1):
        arr = list(map(int, input().split()))
        for j in range(len(arr)):
            cnt[i] += arr[j]
            cnt[j+i+1] += arr[j]

    res = 0
    for i in range(N):
        res += cnt[i]*(N-1-cnt[i])

    total = N*(N-1)*(N-2)//6
    print(total-res//2)

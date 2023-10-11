import sys
input = sys.stdin.readline
n, c = map(int, input().split())
arr = [int(input()) for i in range(n)]
arr.sort()
start, end = 1, arr[-1]-arr[0]
res = 0

while start <= end: #BS
    mid = (start+end)//2
    now = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] >= now + mid:
            cnt += 1
            now = arr[i]
    if cnt >= c:
        start = mid+1
        res = mid
    else:
        end = mid-1
print(res)
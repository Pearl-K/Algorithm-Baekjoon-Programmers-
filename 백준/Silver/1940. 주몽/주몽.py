import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt, l, r = 0, 0, n-1

while l < r:
    if arr[l]+arr[r] == m:
        cnt += 1
        l += 1
    elif arr[l]+arr[r] < m:
        l += 1
    else:
        r -= 1
print(cnt)
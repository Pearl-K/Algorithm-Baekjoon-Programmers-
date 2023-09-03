import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = []

l, r = 0, N-1
res = [arr[l], arr[r]]

while r-1 != l:
    den = arr[l] + arr[r]
    if den < 0:
        l += 1
    else:
        r -= 1
    if abs(sum(res)) > abs(arr[l] + arr[r]):
        res = [arr[l], arr[r]]

print(res[0], res[1])

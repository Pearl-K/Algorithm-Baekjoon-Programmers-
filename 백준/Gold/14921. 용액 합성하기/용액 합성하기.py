import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
st = 0
ed = N-1
res = arr[st]+arr[ed]

while st < ed:
    tmp = arr[st]+arr[ed]
    if tmp == 0:
        res = 0
        break
    if abs(tmp) < abs(res):
        res = tmp
    if tmp < 0:
        st += 1
    else:
        ed -= 1
print(res)
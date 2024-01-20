import sys
input = sys.stdin.readline
m, n = map(int, input().split())
snack = list(map(int, input().split()))
s, e = 1, max(snack)
res = 0

while s <= e:
    mid = (s+e)//2
    tmp = 0
    for sn in snack:
        tmp += (sn//mid)
    if tmp >= m:
        s = mid+1
        res = max(res, mid)
    else:
        e = mid-1
print(res)

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]
st, ed = max(money), sum(money)

while st <= ed:
    mid = (st+ed) >> 1
    charge = mid
    cnt = 1
    for i in money: 
        if (charge-i) < 0:
            cnt += 1
            charge = mid
        charge -= i
    if cnt > M:
        st = mid + 1
    else:
        ed = mid - 1
print(mid)
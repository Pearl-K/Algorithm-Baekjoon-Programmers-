import sys
input = sys.stdin.readline
N = int(input())
city = list(map(int, input().split()))
budg = int(input())
st, ed = 0, max(city)

while st <= ed:
    mid = (st+ed)//2
    total = 0
    for c in city:
        if c > mid:
            total += mid
        else:
            total += c
    if total <= budg:
        st = mid+1
    else:
        ed = mid-1
print(ed)
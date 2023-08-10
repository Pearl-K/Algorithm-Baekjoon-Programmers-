import sys
input = sys.stdin.readline
import bisect

x_pnt = []
y_pnt = []
N = int(input())

for i in range(N):
    x, y = map(float, input().split())
    x_pnt.append(x)
    y_pnt.append(y)

Q = int(input())
for i in range(Q):
    target = float(input())
    l, r = bisect.bisect_left(x_pnt, target), bisect.bisect_right(x_pnt, target);
    
    if l == r:
        l -= 1
    if y_pnt[r] > y_pnt[l]:
        print(1)
    elif y_pnt[r] < y_pnt[l]:
        print(-1)
    else:
        print(0)
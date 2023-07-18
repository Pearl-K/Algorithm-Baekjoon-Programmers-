import sys
from math import pi
input = sys.stdin.readline
r, R, n = map(int, input().split())
res = 0

# 도시 간 이동
city = (1/4)*2*pi*r

# in-line, out-line
in_ln = (1/n)*2*pi*(R-r)
out_ln = (1/n)*2*pi*R

if n == 1:
    res = city
else: # out-line, in-line 번갈아 타는 경우, i1 점에서 시작함. 처음엔 무조건 out-line 탐
    if (n-1) % 2 == 0:
        one = ((n-1)//2)*out_ln + ((n-1)//2)*in_ln + (city*n)
    else:
        one = ((n-1)//2+1)*out_ln + ((n-1)//2)*in_ln + (city*n)
    two = city*n + (city + in_ln)*(n-1)
    res = min(one, two)

print(res)
from math import pi
r, R, n = map(int, input().split())
res = 0

# city 간 이동, 안쪽 라인(R-r) 이동, N/S 라인 이동(R)
city = (1/4)*2*pi*r
in_ln = (1/n)*2*pi*(R-r)
out_ln = (1/n)*2*pi*R

if n == 1:
    res = city
else: # out-line & in-line 번갈아 타는 경우 or i점으로만 이동해야 하는 경우
    if (n-1) % 2 == 0:
        one = ((n-1)//2)*out_ln + ((n-1)//2)*in_ln + (city*n)
    else:
        one = ((n-1)//2+1)*out_ln + ((n-1)//2)*in_ln + (city*n)
    two = city*n + (city + in_ln)*(n-1)
    res = min(one, two)
print(res)
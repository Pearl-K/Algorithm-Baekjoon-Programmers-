import sys
input = sys.stdin.readline

x, y, c= map(float, input().split())
s, e = 0, min(x, y)
res = 0

def cal_c(x, y, w) :
  h1 = (x**2-w**2)**0.5
  h2 = (y**2-w**2)**0.5
  c = h1*h2/(h1+h2)
  return c

while e-s > 0.000001:
    w = (s+e)/2
    res = w

    if cal_c(x, y, w) >= c:
        s = w
    else:
        e = w
print(res) #상대오차 생각
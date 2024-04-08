import sys
input = sys.stdin.readline
xli = list(map(int, input().split()))
a, b, c, d, e = map(int, input().split())
new = [a, (b-d), (c-e)]
res = []
for x in xli:
    tmp = (new[0]//3)*(x**3) + (new[1]//2)*(x**2) + new[2]*x
    res.append(tmp)
print(res[1]-res[0])
import sys
input = sys.stdin.readline
n = int(input())
c = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c.sort(reverse=True)
b.sort(reverse=True)
res = 0
if b[0] > c[0]: 
    res = -1
else:
    while b:
        for i in c:
            if b and i < b[-1]:
                continue
            for j in b:
                if i >= j:
                    b.remove(j)
                    break
        res += 1
print(res)
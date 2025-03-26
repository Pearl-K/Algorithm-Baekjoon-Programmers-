import sys
input = sys.stdin.readline
N = int(input())
pos = []
neg = []
zero = 0
one = 0

for _ in range(N):
    n = int(input())
    
    if n > 1:
        pos.append(n)
    elif n < 0:
        neg.append(n)
    elif n == 1:
        one += 1
    else:
        zero = 1

pos.sort()
neg.sort(reverse=True)
res = 0

while pos:
    if len(pos)>=2:
        a = pos.pop()
        b = pos.pop()
        res += a*b
    else:
        res += pos.pop()

while neg:
    if len(neg)>=2:
        a = neg.pop()
        b = neg.pop()
        res += a*b
    else:
        if zero:
            break
        else:
            res += neg.pop()

res += one
print(res)
import sys
input = sys.stdin.readline

G = int(input())
now = [i for i in range(1, 100001)]
past = [i for i in range(1, 100001)]
MAX = 100000
res = []

l, r = 0, 0
while (l < MAX) and (r < MAX):
    tmp = (now[l]**2) - (past[r]**2)

    if tmp == G:
        res.append(now[l])
        r += 1
    elif tmp < G:
        l += 1
    else:
        r += 1

if res:
    print(*res, sep="\n")
else:
    print(-1)
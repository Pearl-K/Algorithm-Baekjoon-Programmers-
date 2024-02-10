import sys
input = sys.stdin.readline

st = input().rstrip()
alp = [[0 for _ in range(26)] for _ in range(len(st))]

for i in range(len(st)):
    idx = ord(st[i])-97
    if i == 0:
        alp[i][idx] += 1
    else:
        alp[i][idx] += 1
        for j in range(26):
            alp[i][j] += alp[i-1][j]

N = int(input())
for i in range(N):
    a, l, r = input().split()
    res = 0
    idx = ord(a)-97

    if int(l) == 0:
        res = alp[int(r)][idx]
    else:
        res = alp[int(r)][idx]-alp[int(l)-1][idx]

    print(res)
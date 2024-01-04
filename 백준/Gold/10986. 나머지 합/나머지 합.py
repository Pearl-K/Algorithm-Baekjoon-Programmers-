import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
pres = [arr[0]]
div = [0]*m
com = 0

for i in range(1, n):
    pres.append(pres[i-1] + arr[i])

for i in range(n):
    pres[i] %= m
    div[pres[i]] += 1

for i in range(m):
    if div[i] < 2:
        continue
    else:
        com += div[i]*(div[i]-1)//2
print(com+div[0])
#print(pres, div)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10)
N = int(input())

def star(n):
    if n == 1:
        return ['*']

    stars = star(n//3)
    sub = []

    for i in stars:
        sub.append(3*i)
    for i in stars:
        sub.append(i + " "*(n//3) + i)
    for i in stars:
        sub.append(3*i)

    return sub

res = star(N)
for row in res:
    print(''.join(row))
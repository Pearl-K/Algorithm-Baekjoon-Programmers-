import sys
input = sys.stdin.readline
N = int(input())
res =""

while N > 0:
    R = N%2
    N = N//2
    if R == 0:
        N -= 1
        res = '7'+ res
    else:
        res = '4'+ res
print(res)
import sys
input = sys.stdin.readline
N, A, B, C = map(int, input().split())

from math import factorial
def bc(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

res = bc(N, A)*bc(N-A, B)
print(res)
import sys
input = sys.stdin.readline

import math
from decimal import Decimal

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
K = list(map(Decimal, input().split()))

adv = 0
for i in range(N):
    adv += max(math.floor(A[i]*K[i]-B[i]), A[i]-math.floor(B[i]*K[i]))

print(adv)
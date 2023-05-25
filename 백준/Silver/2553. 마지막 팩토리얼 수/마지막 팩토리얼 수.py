import sys
import math
input = sys.stdin.readline
N = int(input())
a = str(math.factorial(N))
for i in a[::-1]:
    if i == '0':
        continue
    else:
        print(i)
        break
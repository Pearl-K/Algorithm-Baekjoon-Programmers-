import sys
import math
N = int(sys.stdin.readline())
result = str(math.factorial(N))
result = result[::-1]
i = 0
if result[i] == '0':
    while result[i] == '0':
        i += 1
    print(i)
else:
    print(0)
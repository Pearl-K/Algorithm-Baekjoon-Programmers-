import sys
input = sys.stdin.readline
N = int(input())
MAX = 2000001
num = [i for i in range(MAX)]
num[1] = 0 #1은 소수 아님

def palin(x):
    a = list(str(x))
    s = 0
    e = len(a) - 1

    while s < e:
        if a[s] != a[e]:
            return False
        s += 1
        e -= 1
    return True

import math
sqrt = int(math.sqrt(MAX))+1

for i in range(2, sqrt):
    if num[i] == 0:
        continue
    for j in range(i+i, MAX, i):
        num[j] = 0

idx = N
while True:
    if num[idx] != 0:
        if palin(idx):
            print(idx)
            break
    idx += 1

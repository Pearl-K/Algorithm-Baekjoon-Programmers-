import sys
input = sys.stdin.readline
A, B = map(int, input().split())
arr = [0]*(10**7 + 1)
a_len = len(arr)

for i in range(2, a_len):
    arr[i] = i

import math
for i in range(2, int(math.sqrt(a_len + 1))):
    if arr[i] == 0:
        continue
    for j in range(i+i, a_len, i):
        arr[j] = 0

res = 0
for i in range(2, 10**7+1):
    if arr[i] != 0:
        tmp = arr[i]
        while arr[i] <= B/tmp:
            if arr[i] >= A/tmp:
                res += 1
            tmp *= arr[i]

print(res)
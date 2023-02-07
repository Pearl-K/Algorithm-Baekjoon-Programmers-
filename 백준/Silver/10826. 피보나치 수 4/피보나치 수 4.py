import sys
n = int(sys.stdin.readline())
result = [0, 1]
if n == 0:
    print(0)
elif n== 1:
    print(1)
else:
    for i in range(2, n + 1):
        result.append(result[i - 1] + result[i - 2])
    print(result[-1])
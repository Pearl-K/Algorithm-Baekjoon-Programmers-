import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
res = [0]*N
INF = sys.maxsize
for i in range(N-1):
    MAX = -float(INF)
    for j in range(i+1, N):
        slope = (arr[j] - arr[i])/(j-i)
        if slope <= MAX:
            continue
        MAX = max(MAX, slope)
        res[i] += 1
        res[j] += 1
print(max(res))
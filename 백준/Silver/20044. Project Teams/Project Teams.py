import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort() #학생수 2n
res = []
for i in range(N):
    res.append(arr[i] + arr[-1-i])
print(min(res))
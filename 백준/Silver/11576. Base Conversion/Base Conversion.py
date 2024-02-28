import sys
input = sys.stdin.readline

a, b = map(int, input().split())
N = int(input())
arr = list(map(int, input().split()))
arr = arr[::-1]

tmp = 0
for i in range(N):
    tmp += arr[i]*(a**i)

res = []
while tmp !=0:
    res.append(tmp%b)
    tmp //= b

res = res[::-1]
print(*res)
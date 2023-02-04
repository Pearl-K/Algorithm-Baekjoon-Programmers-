import sys
N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
res = 0
m = price[0]
for i in range(N-1):
    if price[i] < m:
        m = price[i]
    res += m*road[i]
print(res)
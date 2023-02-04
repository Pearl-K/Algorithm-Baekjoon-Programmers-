import sys
N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(N-1):
    if price[i] < price[i+1]:
        result += price[i]*(road[i]+road[i+1])
        if (i + 1) == len(road) - 1:
            break
    else:
        result += price[i]*road[i]
print(result)
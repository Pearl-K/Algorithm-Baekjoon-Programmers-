import sys
input = sys.stdin.readline
N = int(input())

arr = []
for i in range(N):
    p, d = map(int, input().split())
    arr.append((p, d))

arr.sort(key=lambda x:(-x[0], x[1]))
price = [0]*10001

for i in range(N):
    nowp, nowd = arr[i][0], arr[i][1]

    for j in range(nowd, 0, -1):
        if price[j] == 0:
            price[j] = nowp
            break
print(sum(price))

import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort(key=lambda x:x[2], reverse=True)

print(arr[0][0], arr[0][1])
print(arr[1][0], arr[1][1])

now = 2
while now < n:
    if arr[0][0] == arr[1][0] == arr[now][0]:
        now += 1
    else:
        print(arr[now][0], arr[now][1])
        break
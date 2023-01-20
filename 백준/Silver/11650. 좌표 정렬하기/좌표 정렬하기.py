import sys
input = sys.stdin.readline

num = int(input())

arr = []

for i in range(num):
    [a,b] = map(int, input().split())
    arr.append([a,b])

new_arr = sorted(arr)

for i in range (num):
    print(new_arr[i][0], new_arr[i][1])
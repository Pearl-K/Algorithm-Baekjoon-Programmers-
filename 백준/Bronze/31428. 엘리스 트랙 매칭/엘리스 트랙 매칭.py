import sys
input = sys.stdin.readline
N = int(input())
cnt = [0]*4

arr = list(input().split())
hr = input().rstrip()

for i in range(len(arr)):
    if arr[i] == 'C':
        cnt[0] += 1
    elif arr[i] == 'S':
        cnt[1] += 1
    elif arr[i] == 'I':
        cnt[2] += 1
    else:
        cnt[3] += 1

if hr == 'C':
    print(cnt[0])
elif hr == 'S':
    print(cnt[1])
elif hr == 'I':
    print(cnt[2])
else:
    print(cnt[3])
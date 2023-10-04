import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
rev_arr = arr[::-1] #리버스 arr로 가장 긴 감소하는 수열 구하기
incr = [1 for i in range(n)]
decr = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            incr[i] = max(incr[i], incr[j]+1)
        if rev_arr[i] > rev_arr[j]:
            decr[i] = max(decr[i], decr[j]+1)

res = [0 for i in range(n)]
for i in range(n):
    res[i] = incr[i] + decr[n-i-1]-1
print(max(res))
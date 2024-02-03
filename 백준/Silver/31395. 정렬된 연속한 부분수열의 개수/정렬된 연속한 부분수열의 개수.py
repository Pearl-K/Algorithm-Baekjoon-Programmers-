import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
asc = [1]

for i in range(N-1):
    if arr[i] < arr[i+1]:
        asc.append(asc[-1] + 1)
    else:
        asc.append(1)

print(sum(asc))
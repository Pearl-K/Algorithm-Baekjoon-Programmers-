import sys
input = sys.stdin.readline
N, M = map(int, input().split())
n_list = list(map(int, input().split()))
prefix_sum = [0]
temp = 0
for i in n_list:
    temp += i
    prefix_sum.append(temp)

for k in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
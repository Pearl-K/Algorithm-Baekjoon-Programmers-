import sys
input = sys.stdin.readline
M = int(input())
color = list(map(int, input().split()))
K = int(input())

total = sum(color)
p = [0]*51
res = 0

for i in range(M):
    if color[i] >= K:
        p[i] = 1
        for k in range(K):
            p[i] = (color[i]-k)/(total-k)*p[i]
        res += p[i]
print(res)
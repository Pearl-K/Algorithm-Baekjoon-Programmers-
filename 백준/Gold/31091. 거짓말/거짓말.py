import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = [[0]*500002 for i in range(2)]

for i in range(n):
    if arr[i] > 0:
        cnt[1][arr[i]] += 1
    else:
        cnt[0][-arr[i]] += 1

pre_s = 0
for i in range(1, n+1):
    pre_s += cnt[1][i]

res = []
for i in range(n+1):
    if pre_s == i:
        res.append(i)
    pre_s += cnt[0][i]
    pre_s -= cnt[1][i+1]

print(len(res))
print(*res)

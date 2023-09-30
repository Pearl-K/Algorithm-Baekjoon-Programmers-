import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

# 누적합 arr 만들기
pre_n = []
pre_m = []

for i in range(n):
    now = n_arr[i]
    pre_n.append(now)
    for j in range(i+1, n):
        now += n_arr[j]
        pre_n.append(now)

for i in range(m):
    now = m_arr[i]
    pre_m.append(now)
    for j in range(i+1, m):
        now += m_arr[j]
        pre_m.append(now)

pre_n.sort()
pre_m.sort()
res = 0

import bisect as bs
for i in range(len(pre_n)):
    left = bs.bisect_left(pre_m, t-pre_n[i])
    right = bs.bisect_right(pre_m, t-pre_n[i])
    res += right - left
print(res)
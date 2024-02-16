import sys
input = sys.stdin.readline
N = int(input())
li = []

for _ in range(N):
    s, e = map(int, input().split())
    li.append((s, e))

tmp = 0
li.sort()
st, ed = li[0][0], li[0][1]

for i in range(1, N):
    if li[i][0] <= ed < li[i][1]:
        ed = li[i][1]
    elif ed < li[i][0]:
        tmp += (ed-st)
        st = li[i][0]
        ed = li[i][1]

res = tmp+(ed-st)
print(res)
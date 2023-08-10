import sys
input = sys.stdin.readline

N = int(input())
arr = []
visit = [False] * 1001
res = 0

for i in range(N):
    d, w = map(int, input().split())
    arr.append((d, w))

arr.sort(key=lambda x: x[1], reverse=True)

for day, worth in arr:
    idx = day

    #가능한 날짜 체크
    while idx > 0 and visit[idx]:
        idx -= 1

    if idx == 0:
        continue
    else:
        visit[idx] = True
        res += worth

print(res)
N, M = map(int, input().split())
eggs = []
for i in range(M):
    eggs.append(int(input()))
eggs.sort()
cnt, result, a = 0, 0, 0
for i in range(M):
    cnt = min(M-i, N)
    if result < eggs[i]*cnt:
        result = eggs[i]*cnt
        a = eggs[i]
print(a, result)
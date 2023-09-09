import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

def find_p(x):
    if parent[x] == x:
        return x
    x = find_p(parent[x])
    return x

def union(x, y):
    x = find_p(x)
    y = find_p(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

INF = sys.maxsize
ppl = [[INF for j in range(N+1)] for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    ppl[a][b] = 1
    ppl[b][a] = 1

for i in range(1, N+1):
    ppl[i][i] = 0

def floyd():
    for r in range(1, N+1):
        for p in range(1, N+1):
            for q in range(1, N+1):
                if ppl[p][q] > ppl[p][r] + ppl[r][q]:
                    ppl[p][q] = ppl[p][r] + ppl[r][q]

floyd()
for i in range(N+1):
    for j in range(N+1):
        if ppl[i][j] == INF:
            ppl[i][j] = 0

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if ppl[i][j] >= 1:
            union(i, j)

p_set = set(parent[1:])
p_list = list(p_set)
p_len = len(p_list)
print(p_len)
res = []
for i in range(p_len):
    tmp = INF
    tmpidx = -1
    for j in range(1, N+1):
        if p_list[i] == parent[j] and tmp > max(ppl[j]): #같은 위원회
            tmp = max(ppl[j])
            tmpidx = j
    res.append(tmpidx)
res.sort()
print(*res, sep="\n")
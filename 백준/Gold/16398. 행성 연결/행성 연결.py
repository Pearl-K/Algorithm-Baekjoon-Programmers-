import sys
input = sys.stdin.readline

N = int(input())
matrix = []
edges = []
par = [i for i in range(N+1)]

def find_p(me):
    if par[me] != me:
        par[me] = find_p(par[me])
    return par[me]

def union(u, v):
    u = find_p(u)
    v = find_p(v)
    if u < v: #더 작은 값을 기준으로 union
        par[v] = u
    else:
        par[u] = v

def kruskal():
    res = 0
    for i in range(len(edges)):
        cost, x, y = edges[i][0], edges[i][1], edges[i][2]
        if find_p(x) != find_p(y):
            union(x, y)
            res += cost
    return res


for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# 대각선을 기준으로 대칭인 diagonal matrix 라서 
# 절반만 탐색해서 edges에 넣어주기
for i in range(N):
    for j in range(i):
        if i == j:
            continue
        else:
            w = matrix[i][j]
            edges.append((w, i+1, j+1))

edges.sort()
print(kruskal())
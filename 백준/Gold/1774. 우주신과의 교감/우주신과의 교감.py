import sys
input = sys.stdin.readline
N, M = map(int, input().split())
parent = [i for i in range(N+1)]
edges = [0 for i in range(N+1)]

for i in range(1, N+1):
    edges[i] = list(map(int, input().split()))

def cal_dist(pos1, pos2):
    x1, y1, x2, y2 = pos1[0], pos1[1], pos2[0], pos2[1]
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def find_p(parent, x):
    if x != parent[x]:
        parent[x] = find_p(parent, parent[x])
    return parent[x]

def union_p(parent, a, b):
    a = find_p(parent, a)
    b = find_p(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(M):
    a, b = map(int, input().split())
    union_p(parent, a, b)

cand = []
for i in range(1, len(edges)-1):
    for j in range(i+1, len(edges)):
        cand.append([cal_dist(edges[i], edges[j]), i, j])
cand.sort()
res = 0

for c in cand:
    cost, x, y = c[0], c[1], c[2]
    if find_p(parent, x) != find_p(parent, y):
        union_p(parent, x, y)
        res += cost

print("{:.2f}".format(res))
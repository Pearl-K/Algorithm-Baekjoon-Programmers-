import sys
input = sys.stdin.readline
N = int(input())
rec_arr = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    rec_arr.append(((x1, y1), (x2, y2)))
parent = [i for i in range(N)]

def find_p(u):
    if parent[u] != u:
        parent[u] = find_p(parent[u])
    return parent[u]

def union_p(u, v):
    pu = find_p(u)
    pv = find_p(v)
    if pu == pv:
        return
    if pu > pv:
        pu, pv = pv, pu
    parent[pv] = pu

def checkMeet(a, b):
    (x11, y11), (x12, y12) = a
    (x21, y21), (x22, y22) = b
    if x12 < x21 or x22 < x11 or y12 < y21 or y22 < y11:
        return False
    if x11 < x21 and x22 < x12 and y11 < y21 and y22 < y12:
        return False
    if x21 < x11 and x12 < x22 and y21 < y11 and y12 < y22:
        return False
    return True

for i in range(N-1):
    for j in range(i+1, N):
        if checkMeet(rec_arr[i], rec_arr[j]):
            union_p(i, j)

grps = set(find_p(i) for i in range(N))
res = len(grps)

for (x1, y1), (x2, y2) in rec_arr:
    if (x1 == 0 or x2 == 0) and y1 <= 0 <= y2:
        res -= 1
        break

    if (y1 == 0 or y2 == 0) and x1 <= 0 <= x2:
        res -= 1
        break
print(res)
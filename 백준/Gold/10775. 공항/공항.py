import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

G = int(input())
P = int(input())
air = []
for _ in range(P):
    air.append(int(input()))

parent = [i for i in range(G+1)]
def find_p(me):
    if parent[me] == me:
        return me
    parent[me] = find_p(parent[me])
    return parent[me]

res = 0
for i in range(P):
    now = air[i]
    np = find_p(now)

    if np == 0:
        break
    else:
        parent[np] = parent[np-1]
        res += 1
print(res)
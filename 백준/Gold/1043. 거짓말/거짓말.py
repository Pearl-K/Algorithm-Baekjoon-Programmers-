import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
T = list(map(int, input().split()))
res = 0
parent = [i for i in range(0, N+1)]
party = []
# 과장된 이야기를 할 수 있는 파티 개수 최대니까
# 진실을 알고있는 애랑 parent 같으면 무조건 진실만 말하게

def find_p(x):
    if parent[x] == x:
        return x
    else:
        return find_p(parent[x])

def union(a, b):
    a = find_p(a)
    b = find_p(b)

    #a가 더 작게
    if a > b:
        a, b = b, a

    if a != b:
        parent[b] = a

if T[0] != 0:
    for i in range(1, len(T)):
        union(0, T[i])

for _ in range(M):
    mem = list(map(int, input().split()))
    party.append(mem[1:])

    if mem[0] == 1:
        continue
    else:
        for i in range(2, mem[0]+1):
            union(mem[1], mem[i])

for p in party:
    flg = True

    for i in range(len(p)):
        if find_p(p[i]) == 0:
            flg = False
            break

    if flg:
        res += 1
#print(parent)
print(res)
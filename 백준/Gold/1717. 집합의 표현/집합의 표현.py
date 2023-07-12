import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 에러 주의

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
# parent 초기화 : 자기 자신을 부모로

for i in range(M):
    command, a, b = map(int, input().split())

    if command == 0:
        union(a, b)
    else:
        Pa = find_parent(a)
        Pb = find_parent(b)

        if Pa == Pb:
            print('YES')
        else:
            print("NO")
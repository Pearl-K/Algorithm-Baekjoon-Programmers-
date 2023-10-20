t = int(input())

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        cnt[a] += cnt[b]

for i in range(t):
    f = int(input())
    parent = dict()
    cnt = dict()
    
    for j in range(f):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            cnt[a] = 1
        if b not in parent:
            parent[b] = b
            cnt[b] = 1
        union(a, b)
        print(cnt[find(a)])
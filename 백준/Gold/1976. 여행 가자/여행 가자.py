import sys
input = sys.stdin.readline

def find_parent(x):
    if graph[x] < 0:
        return x
    graph[x] = find_parent(graph[x])
    return graph[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x == y:
        return

    if graph[x] < graph[y]:
        graph[y] = x
    elif graph[y] < graph[x]:
        graph[x] = y
    else:
        graph[x] = y
        graph[y] -= 1     
    return

N = int(input())
M = int(input())
graph = [-1]*(N+1)

for start in range(1, N+1):
    for end, isLinked in zip(range(1, N+1), map(int, input().split())):
        if isLinked:
            union(start, end)
path = list(set(map(int, input().split())))
result = "YES"

for i in range(1, len(path)):
    if find_parent(path[0]) != find_parent(path[i]):
        result = "NO"
        break

print(result)
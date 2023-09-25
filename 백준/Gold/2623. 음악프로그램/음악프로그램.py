import sys
input = sys.stdin.readline

N, M = map(int, input().split())

degree = [0]*(N+1)
graph = [[] for i in range(N+1)]

for i in range(M):
    pd = list(map(int, input().split()))
    for j in range(1, pd[0]):
        graph[pd[j]].append(pd[j+1])
        degree[pd[j+1]] += 1

from collections import deque
Q = deque()

for i in range(1, N+1):
    if degree[i] == 0:
        Q.append(i)

res = []
while Q:
    node = Q.popleft()
    res.append(node)

    for i in graph[node]:
        degree[i] -= 1
        if degree[i] == 0:
            Q.append(i)

if len(res) == 0:
    print(0)
elif len(res) != N:
    print(0)
else:
    print(*res, sep="\n")
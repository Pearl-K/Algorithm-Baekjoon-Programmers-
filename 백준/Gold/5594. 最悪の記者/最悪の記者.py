import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
degree = [0]*(N+1)
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

from collections import deque
Q = deque()

for i in range(1, N+1):
    if degree[i] == 0:
        Q.append(i)

res = []
tf = 0
while Q:
    if len(Q)>1: tf = 1
    node = Q.popleft()
    res.append(node)

    for i in graph[node]:
        degree[i] -= 1
        if degree[i] == 0:
            Q.append(i)
print(*res, sep='\n')
print(tf)
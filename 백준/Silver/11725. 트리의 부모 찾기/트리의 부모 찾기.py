import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(N+1)
def dfs(now):
    for i in graph[now]:
        if visited[i] == 0:
            visited[i] = now
            dfs(i)

dfs(1)
print(*visited[2:], sep='\n')
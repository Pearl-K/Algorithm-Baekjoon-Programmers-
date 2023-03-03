import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())
graph = [[] for i in range(N+1)]
Q = deque()

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(N+1)
cnt = 1

def bfs(start_node):
  global cnt

  Q = deque([R])
  visited[R] = 1

  while Q:
    now = Q.popleft()
    graph[now].sort()
    
    for i in graph[now]:
        if visited[i] == 0:
          cnt += 1
          visited[i] = cnt
          Q.append(i)

bfs(R)

for i in range(1, N+1):
    print(visited[i])
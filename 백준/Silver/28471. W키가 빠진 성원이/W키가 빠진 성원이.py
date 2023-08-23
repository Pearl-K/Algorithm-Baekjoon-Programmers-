import sys
input = sys.stdin.readline

N = int(input())
graph = [[0 for i in range(N)] for j in range(N)]
start = (0, 0)

for i in range(N):
    row = list(input().rstrip())
    for j in range(N):
        if row[j] == 'F':
            start = (i, j)
        if row[j] == '#':
            graph[i][j] = 1

dx = [-1, -1, 0, 0, 1, -1, 1] #도착지부터 출발하므로 아래로 내려가는 키를 빼고, 위로 올라가는 키는 넣어야 한다
dy = [-1, 1, -1, 1, 1, 0, -1]

from collections import deque
def bfs(i, j):
    cnt = 0
    Q = deque()
    Q.append((i, j))

    while Q:
        x, y = Q.popleft()
        visited[x][y] = True

        for i in range(7):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and graph[nx][ny] == 0:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    Q.append((nx, ny))
    return cnt

visited = [[False]*N for i in range(N)]
res = bfs(start[0], start[1])
print(res)
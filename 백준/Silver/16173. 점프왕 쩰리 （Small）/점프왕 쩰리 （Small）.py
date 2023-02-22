import sys
N = int(sys.stdin.readline())
zone = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    zone.append(row)

visited = []
for i in range(N):
    visited.append([False]*N)
dx = [1, 0]
dy = [0, 1]

def dfs(x, y, visited):
    if (x >= N) or (x <= -1) or (y >= N) or (y <= -1):
        return 0
    if visited[x][y] == True:
        return 0
    if zone[x][y] == -1:
        print("HaruHaru")
        sys.exit()
    visited[x][y] = True

    for i in range(2):
        nx = x + dx[i]*zone[x][y]
        ny = y + dy[i]*zone[x][y]
        dfs(nx, ny, visited)
    return True

if dfs(0, 0, visited) == True:
    print('Hing')
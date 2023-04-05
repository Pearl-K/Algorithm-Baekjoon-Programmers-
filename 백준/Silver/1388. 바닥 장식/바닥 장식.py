import sys
sys.setrecursionlimit(10 ** 6)

def dfs_horizontal(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == "-":
        graph[x][y] = "x"
        dfs_horizontal(x, y - 1)
        dfs_horizontal(x, y + 1)
        return True
    return False


def dfs_vertical(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == "|":
        graph[x][y] = "x"
        dfs_vertical(x - 1, y)
        dfs_vertical(x + 1, y)
        return True
    return False

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline()))
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == "-":
            dfs_horizontal(i, j)
            cnt += 1
        elif graph[i][j] == "|":
            dfs_vertical(i, j)
            cnt += 1
print(cnt)
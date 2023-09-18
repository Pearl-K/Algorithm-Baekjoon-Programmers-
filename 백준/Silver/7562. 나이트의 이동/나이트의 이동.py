import sys
input = sys.stdin.readline
T = int(input())

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

from collections import deque

def Night_BFS(I, start, goal):
    if start == goal:
        return 0

    visited = [[-1]*I for _ in range(I)]
    Q = deque()
    Q.append((start[0], start[1]))
    visited[start[0]][start[1]] = 0

    while Q:
        x, y = Q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= I-1 and 0 <= ny <= I-1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1

                if nx == goal[0] and ny == goal[1]:
                    return visited[nx][ny]
                else:
                    Q.append((nx, ny))
    return -1

for _ in range(T):
    I = int(input())
    start = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    res = Night_BFS(I, start, goal)
    print(res if res != -1 else 0)
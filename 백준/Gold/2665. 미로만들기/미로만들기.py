import sys
input = sys.stdin.readline

N = int(input())
grid = []
INF = sys.maxsize
for _ in range(N):
    grid.append(list(map(int, input().rstrip())))

import heapq as hq
def dijkstra(r, c):
    Q = []
    dist = [[INF for _ in range(N)] for _ in range(N)]
    dist[0][0] = 0
    hq.heappush(Q, (0, r, c))

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while Q:
        cost, r, c = hq.heappop(Q)
        #print(cost, r, c, dist[r][c])

        if r == N-1 and c == N-1:
            dist[r][c] = cost
            return cost

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if grid[nr][nc] == 1 and dist[nr][nc] > cost:
                    dist[nr][nc] = cost
                    hq.heappush(Q, (cost, nr, nc))
                elif grid[nr][nc] == 0 and dist[nr][nc] > cost+1:
                    dist[nr][nc] = cost+1
                    hq.heappush(Q, (cost+1, nr, nc))

print(dijkstra(0, 0))

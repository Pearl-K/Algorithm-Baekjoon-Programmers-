import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

def Floyd_W(graph, n):
    for k in range(n):
        for p in range(n):
            for q in range(n):
                if graph[p][q] > graph[p][k] + graph[k][q]:
                    graph[p][q] = graph[p][k] + graph[k][q]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = INF

Floyd_W(graph, N)

for i in range(N):
    for j in range(N):
        if graph[i][j] != INF:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
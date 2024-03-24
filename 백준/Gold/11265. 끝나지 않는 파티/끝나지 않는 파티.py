import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dist = []

for _ in range(N):
    dist.append(list(map(int, input().split())))

for r in range(N):
    for p in range(N):
        for q in range(N):
            if p == q:
                continue
            else:
                if dist[p][q] > dist[p][r] + dist[r][q]:
                    dist[p][q] = dist[p][r] + dist[r][q]
#print(dist)

for _ in range(M):
    a, b, c = map(int, input().split())
    if dist[a-1][b-1] > c:
        print("Stay here")
    else:
        print("Enjoy other party")
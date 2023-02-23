import sys
N = int(sys.stdin.readline())
rank = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    rank.append((x, y))

for i in range(N):
    cnt = 0
    for j in range(N):
        if rank[i][0] < rank[j][0] and rank[i][1] < rank[j][1]:
            cnt += 1
    print(cnt+1, end=' ')
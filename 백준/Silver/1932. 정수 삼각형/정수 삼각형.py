import sys
input = sys.stdin.readline
tri = []
N = int(input())

for i in range(N):
    tri.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(0, i+1):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[N-1]))
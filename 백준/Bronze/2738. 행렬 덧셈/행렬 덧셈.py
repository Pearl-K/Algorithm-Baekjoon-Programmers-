N, M = map(int, input().split())
matrix = []

for i in range(N):
    a = list(map(int, input().split()))
    matrix.append(a)

for i in range(N):
    b = list(map(int, input().split()))
    for j in range(M):
        matrix[i][j] += b[j]

for i in range(N):
    print(*matrix[i])
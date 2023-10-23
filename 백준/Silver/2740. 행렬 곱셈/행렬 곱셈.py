import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
m, k = map(int, input().split())
B = [list(map(int, input().split())) for i in range(m)]

res = [[0 for i in range(k)] for j in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            res[i][j] += A[i][l]*B[l][j]

for row in res:
    print(*row)
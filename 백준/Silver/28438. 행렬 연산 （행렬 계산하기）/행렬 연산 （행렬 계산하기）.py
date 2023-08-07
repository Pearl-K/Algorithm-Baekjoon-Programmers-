import sys
input = sys.stdin.readline
N, M, Q = map(int, input().split())
R = [0]*N
C = [0]*M

for i in range(Q):
    a, b, c = map(int, input().split())
    if a == 1:
        R[b-1] += c
    else:
        C[b-1] += c

for i in range(N):
    for j in range(M):
        print(R[i] + C[j], end=' ')
    print()
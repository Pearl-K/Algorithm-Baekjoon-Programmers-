import sys
N, M = map(int, sys.stdin.readline().split())
passwords = {}
for i in range(N):
    a, b = sys.stdin.readline().split()
    passwords[a] = b

for j in range(M):
    a = sys.stdin.readline().rstrip()
    if a in passwords:
        print(passwords[a])
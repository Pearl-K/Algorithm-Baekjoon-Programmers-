import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().rstrip()

Pn = 'IO'*N + 'I'
lenP = len(Pn)
cnt = 0
for i in range(M - lenP + 1):
    if S[i:i+lenP] == Pn:
        cnt += 1
print(cnt)
import sys
input = sys.stdin.readline
N, K, M = map(int, input().split())
arr = list(map(int,input().split()))

for _ in range(M):
    now = int(input())
    if now > 0:
        if K <= now:
            K = now-K+1
    else:
        if K > now+N:
            K = N+now - (K-1-N)
print(K)
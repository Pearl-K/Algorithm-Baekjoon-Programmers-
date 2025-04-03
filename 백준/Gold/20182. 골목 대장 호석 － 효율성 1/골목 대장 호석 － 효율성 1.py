import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq as hq
N, M, A, B, C = map(int, input().split())
G, D = defaultdict(list),[2000000]*(N+1)
for _ in range(M):
    u,v,w=map(int, input().split())
    G[u].append((v,w))
    G[v].append((u,w))
    
h = [(0,0,A)]

while h:
    m, s, u = hq.heappop(h)
    if u==B:
        print(m)
        sys.exit()
    for v,w in G[u]:
        t = max(m,w)
        if D[v]>t and s+w<=C:
            D[v]=t
            hq.heappush(h, (t, s+w, v))
print(-1)
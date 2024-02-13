import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

N = int(input())
tree = [[] for _ in range(N+1)] #root는 1번
MAX_DEPTH = 100000
MAX_LOG = 17 #int(math.log(MAX_DEPTH, 2)) + 1

for i in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 1. dfs로 깊이 탐색
# 2. ANC[logK][N] 만들어서 채우기 (sparse table)
# 3. LCA 찾기
vst = [False for i in range(N+1)]
depth = [0 for i in range(N+1)]

# ANC[logK][N], c++이면 저런 형태가 캐시접근에서 더 빠름 파이썬은 몰?루
ANC = [[-1]*(N+1) for _ in range(MAX_LOG)]

#일단 모든 노드에 대해 바로 위 부모는 구해야 하네..?
#dfs로 전체 depth와 ANC[0] 값 채우기(자기보다 2**0 위에 있는 노드)
def dfs(node, d):
    vst[node] = True
    depth[node] = d
    for next in tree[node]:
        if not vst[next]:
            ANC[0][next] = node
            dfs(next, d+1)
dfs(1, 0)

for k in range(1, MAX_LOG):
    for node in range(1, N+1):
        ANC[k][node] = ANC[k-1][ANC[k-1][node]]

def LCA(u, v):
    if depth[u] < depth[v]: #u가 depth 더 깊게 조정하기
        u, v = v, u
    d_diff = depth[u]-depth[v]

    kcnt = 0
    while d_diff:
        if d_diff & 1:
            u = ANC[kcnt][u] #더 밑에 있는 노드 u를 조상으로 바꿔주면서 끌어올리기
        kcnt += 1
        d_diff >>= 1

    if u == v:
        return u

    for i in range(MAX_LOG-1, -1, -1):
        if ANC[i][u] != ANC[i][v]:
            u = ANC[i][u]
            v = ANC[i][v]

    return ANC[0][u]

M = int(input())
for i in range(M):
    u, v = map(int, input().split())
    print(LCA(u, v))
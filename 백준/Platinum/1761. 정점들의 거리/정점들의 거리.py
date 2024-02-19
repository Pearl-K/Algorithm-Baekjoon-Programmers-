#1. 트리와 가중치를 받는다
#2. ANC 테이블을 채우는데, dist도 같이하기(sparse table) -> LCA를 구한다
#3. D1 + D2 구하기(D는 LCA까지의 거리)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
MAX_DEPTH = 40000
MAX_LOG = 17

tree = [[] for _ in range(N+1)]
vst = [False for _ in range(N+1)]
depth = [0]*(N+1)
ANC = [[[0, 0] for _ in range(N+1)] for _ in range(MAX_LOG)]

for i in range(N-1):
    u, v, w = map(int, input().split())
    tree[u].append([v, w])
    tree[v].append([u, w])

def dfs(node, d):
    vst[node] = True
    depth[node] = d
    for next, dist in tree[node]:
        if not vst[next]:
            ANC[0][next][0] = node
            ANC[0][next][1] = dist #2**0 번째 조상까지의 거리
            dfs(next, d+1)

dfs(1, 0)

#Sparse table 만들 때 dist 계산도 같이?
for k in range(1, MAX_LOG):
    for node in range(1, N+1):
        par = ANC[k-1][ANC[k-1][node][0]][0]
        dist = ANC[k-1][node][1] + ANC[k-1][ANC[k-1][node][0]][1]
        ANC[k][node][0] = par
        ANC[k][node][1] = dist

def LCA(a, b):

    res = 0
    if depth[a] < depth[b]: #a가 더 깊은 곳에 있도록 조정
        a, b = b, a
    diff = depth[a]-depth[b]

    kcnt = 0
    while diff:
        if diff & 1:
            #print(ANC[kcnt][a][1])
            res += ANC[kcnt][a][1] # a 바꾸기전에 dist 더해줘야함
            a = ANC[kcnt][a][0]

        kcnt += 1
        diff >>= 1

    if a == b:
        return res

    for k in range(MAX_LOG-1, -1, -1):
        if ANC[k][a][0] != ANC[k][b][0]:
            #print(ANC[k][a][1], ANC[k][b][1])
            res += (ANC[k][a][1] + ANC[k][b][1]) #갱신 전에 거리 더해주기..
            a = ANC[k][a][0]
            b = ANC[k][b][0]

    #print(ANC[0][a][0], ANC[0][b][0])
    #print(ANC[0][a][1], ANC[0][b][1])
    res += ANC[0][a][1]
    res += ANC[0][b][1]
    return res

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
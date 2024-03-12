import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
vst = [False]*(N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

flg = False
def dfs(now, depth):
    global flg
    if depth == 5:
        flg = True
        return
    
    vst[now] = True
    for next in graph[now]:
        if not vst[next]:
            dfs(next, depth+1)
    vst[now]= False

for i in range(N):
    dfs(i, 1)
    if flg:
        break
print(1 if flg else 0)

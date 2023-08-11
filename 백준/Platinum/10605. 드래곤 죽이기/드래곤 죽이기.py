import sys
input = sys.stdin.readline

def solve(n, m, k):
    vis = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    dragon = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for _ in range(k):
        C, S, N = map(int, input().split())
        dragon[C].append((N, S))

    ans = 0
    for i in range(1, n + 1):
        if vis[i]:
            continue
        d = []
        q = [i]
        vis[i] = 1
        while q:
            cur = q.pop(0)
            for x in dragon[cur]:
                d.append(x)
            for nx in graph[cur]:
                if not vis[nx]:
                    vis[nx] = 1
                    q.append(nx)
        d.sort(reverse=True)
        add = 0
        for j in range(len(d)):
            if add > d[j][0]:
                break
            add = min(add + d[j][1], d[j][0] + 1)
        ans += add
    print(ans)


while True:
    n, m, k = map(int, input().split())
    if n == 0:
        break
    solve(n, m, k)

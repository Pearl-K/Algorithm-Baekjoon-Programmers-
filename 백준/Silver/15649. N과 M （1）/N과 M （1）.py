import sys
N, M = map(int, sys.stdin.readline().split())
result = []
num = [(i+1) for i in range(N)]

def dfs(): #백트래킹은 dfs의 일종
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()

dfs()
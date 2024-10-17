# 문제 접근
# 1. 사이클 그래프 찾기
# 2. 사이클 그래프로부터 각 노드 도달거리 탐색하기
# 알고리즘

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
MAX = 3001

N = int(input())
graph = [[] for _ in range(N+1)]
cycle = [MAX] * (N+1) # 사이클까지 각 노드 도달 거리
vst = [False]*(N+1)

for i in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

flg = 0
def find_cycle(path, cnt): # 지나온 노드 path, 깊이
    global flg
    if flg: # 발견한 경우에 리턴
        return

    # 현재 노드(path의 마지막 노드)와 연결된 노드 탐색
    for i in graph[path[-1]]:
        if i == path[0] and cnt >= 2: # 사이클인 경우 종료
            for j in path:
                cycle[j] = 0 # j 노드는 사이클에 속하는 노드
            flg = 1
            return

        if not vst[i]:
            vst[i] = True
            find_cycle(path + [i], cnt + 1)
            vst[i] = False

for i in range(1, N+1):
    vst[i] = 1
    find_cycle([i], 0)
    vst[i] = 0

# 사이클에 속하는 노드 BFS 돌리기
from collections import deque
Q = deque()

for i in range(1, N+1):
    if cycle[i] == 0:
        Q.append((i, 0))

while Q:
    now, d = Q.popleft()
    for v in graph[now]:
        if cycle[v] == MAX:
            cycle[v] = d+1
            Q.append((v, d+1))

print(*cycle[1:])
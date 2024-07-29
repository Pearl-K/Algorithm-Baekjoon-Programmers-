import sys
input = sys.stdin.readline

#위상정렬과 dp를 이용한 최소 시간 찾기
#위상정렬을 사용하는 것은 쉽지만 dp 상태와 전이를 생각해서 cost를 잘 찾도록
N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
cost = [0 for _ in range(N+1)]

for i in range(1, N+1):
    li = list(map(int, input().split()))[:-1]
    cost[i] = li[0]

    for node in li[1:]:
        graph[node].append(i)
        indegree[i] += 1

dp = [0 for _ in range(N+1)]
from collections import deque
Q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        Q.append(i)
        dp[i] = cost[i]

while Q:
    now = Q.popleft()

    for next in graph[now]:
        indegree[next] -= 1
        dp[next] = max(dp[next], dp[now]+cost[next])

        if indegree[next] == 0:
            Q.append(next)

for i in range(1, N+1):
    print(dp[i])

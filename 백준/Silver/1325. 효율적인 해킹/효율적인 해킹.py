import sys
input = sys.stdin.readline
n, m = map(int, input().split())

from collections import deque
def BFS(start):
	cnt = 1
	q = deque([start])
	vst = [False for _ in range(n+1)]
	vst[start] = True

	while q:
		now = q.popleft()
		for next in graph[now]:
			if not vst[next]:
				vst[next] = True
				cnt += 1
				q.append(next)
	return cnt

graph = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[b].append(a) #단방향 신뢰임 주의

max_c = 1
res = []

for i in range(1, n+1):
	cnt = BFS(i)
	if cnt > max_c:
		max_c = cnt
		res = []
		res.append(i)
	elif cnt == max_c:
		res.append(i)
print(*res)
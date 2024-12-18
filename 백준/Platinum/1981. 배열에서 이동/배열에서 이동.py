import sys
from collections import deque
input = sys.stdin.readline
MIN = 201
MAX = -1
dr = [-1, 1, 0 ,0]
dc = [0, 0, -1, 1]

N = int(input())
grid = []

for _ in range(N):
    line = list(map(int, input().split()))
    for n in line:
        MIN = min(MIN, n)
        MAX = max(MAX, n)
    grid.append(line)

s, e = grid[0][0], grid[N-1][N-1]

# 이분 탐색을 위한 check 함수
def check_mid(mid): 
    for i in range(MIN, MAX + 1):
        if not (i <= s <= i + mid and i <= e <= i + mid):
            continue

        if bfs(i, i + mid):  # 간격을 bfs 함수로 넘기기
            return True
    return False

def bfs(st, ed):
    vst = [[False] * N for _ in range(N)]
    vst[0][0] = True
    queue = deque([(0, 0)])
    
    while queue:
        r, c = queue.popleft()
        
        if r == N-1 and c == N-1:  # 도착
            return True

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not vst[nr][nc]:
                if st <= grid[nr][nc] <= ed:  # 범위 내에 있는 값만 큐에 추가
                    vst[nr][nc] = True
                    queue.append((nr, nc))

    return False

l, r = 0, MAX
res = 0

# binary search
while l <= r:
    mid = (l + r) // 2
    if check_mid(mid):
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)
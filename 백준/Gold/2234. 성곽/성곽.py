from collections import deque
import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
s = [list(map(int, input().split())) for i in range(M)]
vst = [[0]*N for i in range(M)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    vst[x][y] = 1
    room = 1
      
    while q:
        x, y = q.popleft()
        wall = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((s[x][y] & wall) != wall): 
                if 0<=nx<M and 0<=ny<N and not vst[nx][ny]:
                    room+=1
                    vst[nx][ny] = 1
                    q.append((nx,ny))
            wall = wall*2
    return room
    
room_cnt = 0
room_max = 0
room_del = 0

for i in range(M):
    for j in range(N):
        if vst[i][j] == 0:
            room_cnt += 1
            room_max = max(room_max, bfs(i, j))

for i in range(M):
    for j in range(N):
        num = 1
        while num < 9:
            if num & s[i][j]:
                vst = [[0] * N for _ in range(M)]
                s[i][j] -= num
                room_del = max(room_del, bfs(i, j))
                s[i][j] += num
            num *= 2
            
print(room_cnt)
print(room_max)
print(room_del)
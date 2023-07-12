from collections import deque

def bfs(i, j, R, C, visited, maps): #너비 우선 탐색을 통한 무인도 식량 파악
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    Q = deque()
    
    if visited[i][j] == True:
        return 0  
    else:
        Q.append((i, j))
        visited[i][j] = True
        cnt += int(maps[i][j])
    
        while Q:
            x, y = Q.popleft()
            
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
        
                if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == False and maps[nx][ny] != 'X':
                    cnt += int(maps[nx][ny])
                    visited[nx][ny] = True
                    Q.append((nx, ny))
                
        return cnt
                  
    
def solution(maps):
    answer = []
    R = len(maps)
    C = len(maps[0])
    visited = [[False]*C for x in range(R)] #방문 처리를 위한 배열
    res = 0
    
    for i in range(R):
        for j in range(C):
            if maps[i][j] != 'X':
                res = bfs(i, j, R, C, visited, maps)
                if res != 0:
                    answer.append(res)
    
    answer.sort() #배열 오름차순 정렬
    
    if answer:
        return answer
    else:
        answer = [-1]
        return answer
 
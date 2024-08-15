#import sys
#input = sys.stdin.readline
#삼성은 sys 사용 불가...

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    grid = []
    ret = 0
    MAX = 0

    for i in range(N):
        grid.append(list(map(int, input().split())))
        MAX = max(MAX, max(grid[i])) #최대 높이 갱신

    #시작지 정보 저장
    start = []

    for i in range(N):
        for j in range(N):
            if grid[i][j] == MAX:
                start.append((i, j))


    def dfs(x, y, path, k):
        global ret

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < N) and not vst[nx][ny]:
                if grid[x][y] > grid[nx][ny]:
                    vst[nx][ny] = True
                    dfs(nx, ny, path+1, k)
                    vst[nx][ny] = False

                elif k == 0:
                    tmp = grid[nx][ny]
                    if grid[nx][ny] - grid[x][y] < K:
                        grid[nx][ny] = grid[x][y] - 1
                        # 최대한 차이가 적게 나게 깎아야 함
                        # 근데 값을 함부로 바꾸면 다음 깎아야 할 때 문제 발생

                        vst[nx][ny] = True
                        dfs(nx, ny, path+1, k+1)
                        vst[nx][ny] = False
                        grid[nx][ny] = tmp #원래대로 되돌려주기

        ret = max(ret, path)
        return

    for i, j in start:
        vst = [[False]*N for _ in range(N)]
        vst[i][j] = True
        dfs(i, j, 1, 0) #좌표 x, y, 등산로 길이, 공사 여부

    print("#"+str(t)+" "+str(ret))
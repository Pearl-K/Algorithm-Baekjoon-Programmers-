fds = dict()
g_score = dict()

def solution(friends, gifts):
    N = len(friends)
    M = len(gifts)
    grid = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        name = friends[i]
        fds[name] = i
        g_score[i] = 0
    
    for i in range(M):
        a, b = gifts[i].split(" ")
        
        aidx = fds[a]
        bidx = fds[b]
        grid[aidx][bidx] += 1
        g_score[aidx] += 1
        g_score[bidx] -= 1
    
    now_gift = [0 for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i != j:
                if(grid[i][j] > grid[j][i]): 
                    now_gift[i] += 1
                if(grid[i][j] == grid[j][i] or (grid[i][j] == 0 and grid[j][i] == 0)):
                    if(g_score[i] > g_score[j]): now_gift[i] += 1
    
    res = max(now_gift)
    return res
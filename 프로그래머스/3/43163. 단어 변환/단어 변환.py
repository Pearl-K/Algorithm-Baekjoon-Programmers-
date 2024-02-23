from collections import deque

def bfs(begin, target, words):
    
    Q = deque()
    Q.append([begin, 0])
    
    while Q:
        nw, dist = Q.popleft()
        
        if nw == target:
            return dist
        
        for w in words:
            cnt = 0
            for i in range(len(nw)):
                if nw[i] != w[i]:
                    cnt += 1
            if cnt == 1:
                Q.append([w, dist+1])
    return 0
    
    
def solution(begin, target, words):
    
    #edge case
    flg = False
    for w in words:
        if target == w:
            flg = True
    
    if not flg:
        return 0
    
    res = bfs(begin, target, words)
    return res
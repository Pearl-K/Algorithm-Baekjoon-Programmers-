import sys
INF = sys.maxsize

def dfs(a, b, idx, info, n, m, dp):
    global res
    if idx == len(info):
        if a < n and b < m:
            res = min(res, a)
        return
    
    if (a, b, idx) not in dp:
        dp.add((a, b, idx))
    else:
        return
    
    if a >= n or b >= m or a >= res:
        return
    
    dfs(a+info[idx][0], b, idx+1, info, n, m, dp)
    dfs(a, b+info[idx][1], idx+1, info, n, m, dp)
    
    
def solution(info, n, m):
    global res
    res = INF
    dp = set()
    dfs(0, 0, 0, info, n, m, dp)
    if res == INF:
        return -1
    else:
        return res
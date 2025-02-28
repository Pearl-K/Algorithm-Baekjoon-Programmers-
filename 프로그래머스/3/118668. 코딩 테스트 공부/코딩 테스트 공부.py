INF = 10**9

def solution(alp, cop, problems):
    goal_alp = 0
    goal_cop = 0
    
    for p in problems:
        goal_alp = max(goal_alp, p[0])
        goal_cop = max(goal_cop, p[1])
    
    dp = [[INF for _ in range(goal_cop+1)] for _ in range(goal_alp+1)]
    
    nalp = min(alp, goal_alp)
    ncop = min(cop, goal_cop)
    
    dp[nalp][ncop] = 0
    
    for i in range(nalp, goal_alp+1):
        for j in range(ncop, goal_cop+1):
            if i < goal_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < goal_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    nxtalp = min(i+alp_rwd, goal_alp)
                    nxtcop = min(j+cop_rwd, goal_cop)
                    dp[nxtalp][nxtcop] = min(dp[nxtalp][nxtcop], dp[i][j]+cost)
    return dp[goal_alp][goal_cop]
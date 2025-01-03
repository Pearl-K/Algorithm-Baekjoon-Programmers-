def solution(info, edges):
    vst = [False] * len(info)
    res = []
    
    # 모든 곳에서 뻗어나갈 수 있는 dfs를 짜는게 관건
    
    def dfs(cnt_sheep, cnt_wolf):
        if cnt_sheep > cnt_wolf:
            res.append(cnt_sheep)
        else: 
            return #양이 잡아먹히므로 종료
        
        for parent, child in edges:
            if vst[parent] and not vst[child]:
                vst[child] = True
                if info[child] == 0:
                    dfs(cnt_sheep+1, cnt_wolf)
                else:
                    dfs(cnt_sheep, cnt_wolf+1)
                vst[child] = False #원복
    
    vst[0] = True
    dfs(1, 0)
    return max(res)
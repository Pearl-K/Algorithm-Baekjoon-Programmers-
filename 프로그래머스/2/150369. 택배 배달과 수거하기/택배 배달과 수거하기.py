def solution(cap, n, deliveries, pickups):
    rev_del = deliveries[::-1]
    rev_pick = pickups[::-1]
    res = 0
    del_cnt = 0
    pick_cnt = 0
    
    for i in range(n):
        del_cnt += rev_del[i]
        pick_cnt += rev_pick[i]
        
        while del_cnt > 0 or pick_cnt > 0:
            del_cnt -= cap
            pick_cnt -= cap
            res += (n-i)*2
    return res
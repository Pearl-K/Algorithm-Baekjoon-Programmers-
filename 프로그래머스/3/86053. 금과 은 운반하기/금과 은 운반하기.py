def solution(a, b, g, s, w, t):
    res = (10**9) * (10**5) * 4
    st = 0
    ed = (10**9) * (10**5) * 4
    
    while st <= ed:
        mid = (st+ed)>>1
        gold = 0
        silver = 0 
        total = 0
        
        for i in range(len(g)):
            ng = g[i]
            ns = s[i]
            nw = w[i]
            nt = t[i]
            cnt = mid //(nt*2)
            
            if mid % (nt*2) >= nt:
                cnt += 1          
            gold += ng if (ng < cnt*nw) else cnt*nw
            silver += ns if (ns < cnt * nw) else cnt*nw
            total += ng + ns if (ng+ns < cnt*nw) else cnt*nw
        
        if gold >= a and silver >= b and total >= a+b:
            ed = mid-1
            res = min(res, mid)
        else:
            st = mid + 1
    return res
        
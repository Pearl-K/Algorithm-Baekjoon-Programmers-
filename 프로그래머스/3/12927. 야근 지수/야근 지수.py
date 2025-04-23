import heapq as hq

def solution(n, works):
    H = []
    for w in works:
        H.append(-w)
    
    hq.heapify(H)
    
    for i in range(n):
        top = hq.heappop(H)
        
        if top == 0:
            break
        else:
            top += 1
            hq.heappush(H, top)
    res = 0
    while H:
        now = hq.heappop(H)
        res += (now**2)
    
    return res
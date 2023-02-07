def solution(s):
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    
    result = []
    
    for i in s:
        new_i = i.split(',')
        for j in new_i:
            if int(j) not in result:
                result.append(int(j))
                
    return result
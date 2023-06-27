import math

def solution(r1, r2):
    #1. 내부 점 찾기
    in_cnt = 0
    
    #2. bound 하한-상한 정해서 찾기
    for x in range(1, r2 + 1):
        y_max = math.floor(math.sqrt(r2**2 - x**2))
        y_min = 0 if x >= r1 else math.ceil(math.sqrt(abs(r1**2 - x**2)))
        in_cnt += y_max - y_min + 1
    
    return in_cnt*4
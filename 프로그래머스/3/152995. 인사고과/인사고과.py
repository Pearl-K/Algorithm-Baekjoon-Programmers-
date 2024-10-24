def solution(scores):
    res = 0
    ta, tb = scores[0]
    target_score = ta + tb

    # 첫번째 점수에 대한 내림차순, 첫 번째 점수가 같으면 두 번째 점수에 대해서 오름차순
    scores.sort(key=lambda x: (-x[0], x[1]))
    tmp_max = 0
    
    for a, b in scores:
        if ta < a and tb < b:
            return -1
        
        if b >= tmp_max:
            tmp_max = b
            if a + b > target_score:
                res += 1
            
    return res + 1
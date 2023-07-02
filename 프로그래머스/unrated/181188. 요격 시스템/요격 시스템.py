def solution(targets):
    answer = 0
    # 1. 끝 순서대로 sorting
    targets.sort(key = lambda x:(x[1], x[0]))
    
    # 2. 초기화
    s = e = 0
    for t in targets:
        if t[0] >= e:
            answer += 1
            e = t[1] #범위 업로드

    return answer
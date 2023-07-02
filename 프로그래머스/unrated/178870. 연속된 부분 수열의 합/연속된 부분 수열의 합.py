# 선형 탐색 + 투 포인터 (l, r)

def solution(sequence, k):
    answers = []
    prefix_s, l, r = 0, 0, -1
    
    while True:
        
        if prefix_s < k: # 부분합이 k보다 작을 때
            r += 1
            if r >= len(sequence):
                break
            prefix_s += sequence[r]
        
        else: #부분합이 k보다 클 때
            prefix_s -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
            
        if prefix_s == k:
            answers.append([l, r])
            
    answers.sort(key = lambda x:(x[1]-x[0], x[0]))
    return answers[0]
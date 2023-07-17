from collections import Counter
def solution(weights):
    answer = 0
    cnt = Counter(weights)
    for k,v in cnt.items():
        if v>=2:
            answer+= v*(v-1)//2
    weights = set(weights) 

    for w in weights:
        if w*2/3 in weights:
            answer+= cnt[w*2/3] * cnt[w]
        if w*2/4 in weights:
            answer+= cnt[w*2/4] * cnt[w]
        if w*3/4 in weights:
            answer+= cnt[w*3/4] * cnt[w]
    return answer
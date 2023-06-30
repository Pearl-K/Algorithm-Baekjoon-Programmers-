def solution(picks, minerals):
    # 1. 곡괭이수 * 5와 광물 개수 비교
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks) * 5]

    cnt = scan_minerals(minerals)
    answer = calculate_fatigue(cnt, picks)
    return answer

def scan_minerals(minerals):
    i = 0
    cnt = []
    flag = True
    while flag:
        target = []
        if i + 5 < len(minerals):
            target = minerals[i:i + 5]
        else:
            target = minerals[i:]
            flag = False
        dias, irons, stones = target.count('diamond'), target.count('iron'), target.count('stone')
        cnt.append([dias, irons, stones])
        i += 5
    cnt.sort(key=lambda x: (-x[0], -x[1]))
    return cnt

def calculate_fatigue(cnt, picks):
    result = 0
    for target in cnt:
        if picks[0] > 0:
            picks[0] -= 1
            result += sum(target)
        elif picks[1] > 0:
            picks[1] -= 1
            result += target[0] * 5 + target[1] + target[2]
        elif picks[2] > 0:
            picks[2] -= 1
            result += target[0] * 25 + target[1] * 5 + target[2]
        else:
            break
    return result
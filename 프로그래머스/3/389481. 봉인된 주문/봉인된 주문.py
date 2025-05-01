from bisect import bisect_left, bisect_right

def solution(n, bans):
    MAX_LEN = 11
    # 1) bans를 길이별로 정렬된 리스트로 분리
    bans_by_len = {L: [] for L in range(1, MAX_LEN+1)}
    for w in bans:
        bans_by_len[len(w)].append(w)
    for L in bans_by_len:
        bans_by_len[L].sort()

    # 2) 목표 문자열의 길이 L 찾기
    length = None
    for L in range(1, MAX_LEN+1):
        total = 26 ** L
        banned = len(bans_by_len[L])
        valid = total - banned
        if n > valid:
            n -= valid
        else:
            length = L
            break

    # 3) 길이 length 안에서 한 글자씩 채워서 n번째 찾기
    prefix = ""
    for pos in range(1, length+1):
        for ci in range(26):
            c = chr(ord('a') + ci)
            p2 = prefix + c
            # 남은 자리수 (남은 자유 알파벳 조합 수)
            rem = length - len(p2)
            total_sub = 26 ** rem

            # bans_by_len[length]에서 "p2"로 시작하는 금지 개수
            arr = bans_by_len[length]
            lo = bisect_left(arr, p2)
            hi = bisect_right(arr, p2 + '{')
            banned_sub = hi - lo

            valid_sub = total_sub - banned_sub
            if n > valid_sub:
                n -= valid_sub
            else:
                # p2 자체가 금지된 길이-L 문자열이면 skip하지 않고
                # 그건 이 서브트리 맨 앞이 아니므로 자리 수 줄이지 않음
                prefix = p2
                break
    return prefix
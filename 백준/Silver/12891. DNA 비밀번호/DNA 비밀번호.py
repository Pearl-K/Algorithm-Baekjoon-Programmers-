import sys
input = sys.stdin.readline
s, p = map(int, input().split())
pw = list(input().rstrip())
min_p = list(map(int, input().split()))
cnt_p = [0]*4

# 처음 문자열 cnt 배열 초기화 O(p)
for i in range(p):
    if pw[i] == 'A':
        cnt_p[0] += 1
    elif pw[i] == 'C':
        cnt_p[1] += 1
    elif pw[i] == 'G':
        cnt_p[2] += 1
    else:
        cnt_p[3] += 1

start, res = 0, 0
def compare_cnt(min_p, cnt_p):
    for i in range(4):
        if min_p[i] <= cnt_p[i]:
            continue
        else:
            return 0
    return 1

def minus_st(cnt_p, start):
    if pw[start] == 'A':
        cnt_p[0] -= 1
    elif pw[start] == 'C':
        cnt_p[1] -= 1
    elif pw[start] == 'G':
        cnt_p[2] -= 1
    else:
        cnt_p[3] -= 1

def plus_end(cnt_p, end):
    if pw[end] == 'A':
        cnt_p[0] += 1
    elif pw[end] == 'C':
        cnt_p[1] += 1
    elif pw[end] == 'G':
        cnt_p[2] += 1
    else:
        cnt_p[3] += 1

while start <= s-p:
    res += compare_cnt(min_p, cnt_p)  # 처음 비교 추가
    minus_st(cnt_p, start)
    start += 1
    if start > s-p:
        break
    plus_end(cnt_p, start+p-1)

print(res)
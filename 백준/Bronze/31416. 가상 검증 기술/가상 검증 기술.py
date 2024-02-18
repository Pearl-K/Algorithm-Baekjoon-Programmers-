import sys
input = sys.stdin.readline
Q = int(input())
INF = sys.maxsize
res = INF

for _ in range(Q):

    ta, tb, va, vb = map(int, input().split())

    tmp = tb*vb #도훈이가 무조건 혼자 하는 시간
    total_a = ta*va #a를 혼자할 때 걸리는 시간

    if va == 1 and vb == 1:
        res = max(ta, tb)
    elif tmp >= total_a:
        res = tmp
    else: # total_a > tmp
        left_va = va - (tmp//ta) #남은 a 개수
        left_at = ta*(va-left_va) #현재 상혁의 소모 시간

        if left_va%2 == 0:
            dh = tmp + ta*(left_va//2)
            sh = left_at + ta*(left_va//2)
            res = max(dh, sh)
        else:
            dh = tmp + ta*(left_va//2) + ta
            sh = left_at + ta*(left_va//2) + ta
            res = min(dh, sh)
    print(res)
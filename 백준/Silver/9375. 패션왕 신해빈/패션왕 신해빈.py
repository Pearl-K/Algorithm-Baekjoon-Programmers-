import sys

T = int(sys.stdin.readline())

# 종류 개수 N + 조합 : type 별로 가능한 조합의 수 찾기
for i in range(T):
    closet = {}
    N = int(sys.stdin.readline())
    for n in range(N):
        a, b = input().split()
        if b not in closet.keys():
            closet[b] = 1
        else:
            closet[b] += 1
    cnt = 1
    for j in closet:
        cnt *= closet[j]+1
    print(cnt-1)
import sys
input = sys.stdin.readline
T = int(input())
MOD = 10**9 + 7

#거듭제곱 빠르게 계산하기
def pow(target):
    a = 2
    b = target
    res = 1
    while b:
        if b % 2 == 1:
            res *= a
            res %= MOD
        a *= a
        a %= MOD
        b //= 2

    return res

for _ in range(T):
    N = int(input())
    if N == 1:
        print(1)
    else:
        print(pow(N-2))
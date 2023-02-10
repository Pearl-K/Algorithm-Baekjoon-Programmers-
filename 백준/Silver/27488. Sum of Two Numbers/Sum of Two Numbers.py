import sys, math, itertools, bisect
input = sys.stdin.readline

def ok(x): print('YES' if x else 'NO')

T = int(input())
for _ in range(T):
    n = input().rstrip()
    k1, k2 = '', ''
    flag = True
    for k in n:
        if int(k) % 2:
            t = int(k) // 2
            if flag:
                flag = False
                k1 += str(t)
                k2 += str(t+1)
            else:
                flag = True
                k1 += str(t+1)
                k2 += str(t)
        else:
            t = int(k) // 2
            k1 += str(t)
            k2 += str(t)
    print(int(k1), int(k2))
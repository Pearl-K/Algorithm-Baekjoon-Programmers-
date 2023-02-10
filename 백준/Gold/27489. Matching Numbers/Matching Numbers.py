import sys
T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    num = [i for i in range(1, 2*n+1)]
    # 1~n 까지의 합
    result = sum(num) - sum(num[0:n])
    center = sum(num)/n
    cnt = []
    if (result % n) == 0:
        if n == 1:
            print('Yes')
            print(*num)
        else:
            print('Yes')
            for j in range(n//2+1):
                print(num[2*j], num[2*n-1-j])
            for z in range(n//2):
                print(num[n-2*(z+1)], num[n+z])
    else:
        print('No')
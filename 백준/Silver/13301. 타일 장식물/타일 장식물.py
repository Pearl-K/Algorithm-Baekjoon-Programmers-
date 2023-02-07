import sys
N = int(sys.stdin.readline())
if N == 1:
    print(1*2 + 1*2)
elif N ==2:
    print(1*2 + 2*2)
else:
    num = [0, 1, 1]
    for i in range(3, N+1):
        num.append(num[i-1] + num[i-2])
    print(num[N]*2 + (num[N]+num[N-1])*2)
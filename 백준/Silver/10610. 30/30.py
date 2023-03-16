import sys
N = list(map(int, sys.stdin.readline().rstrip()))

if not 0 in N:
    print(-1)
else:
    if sum(N)%3 == 0:
        N.sort(reverse=True)
        N = list(map(str, N))
        print(''.join(N))
    else:
        print(-1)
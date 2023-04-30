import sys
input = sys.stdin.readline
N = int(input())

def promising(x):
    for i in range(x):
        if (col[i] == col[x] or abs(col[x]-col[i]) == abs(x-i)):
            return False
    return True

def N_Queens(x):
    global cnt
    if x == N:
        cnt += 1
    else:
        for i in range(N):
            col[x] = i
            if promising(x):
                N_Queens(x+1)
cnt = 0
col = [0]*(N)
N_Queens(0)
print(cnt)
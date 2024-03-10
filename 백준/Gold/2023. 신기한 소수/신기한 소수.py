import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

def prime(x):
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(1, 10):
            if i%2 == 0:
                continue
            elif prime(10*num + i):
                dfs(10*num + i)
dfs(2)
dfs(3)
dfs(5)
dfs(7)
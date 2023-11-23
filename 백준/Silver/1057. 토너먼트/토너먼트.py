import sys
input = sys.stdin.readline
n, s, e = map(int, input().split())
cnt = 0

while s != e :
    s -= s//2
    e -= e//2
    cnt += 1
print(cnt)
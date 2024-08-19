import sys
input = sys.stdin.readline
S = list(input().rstrip())
T = list(input().rstrip())

def check(T):
    while len(S) != len(T):
        if T[-1] == 'A':
            T.pop()
        elif T[-1] == 'B':
            T.pop()
            T = T[::-1]
    if S == T:
        return 1
    else:
        return 0
print(check(T))
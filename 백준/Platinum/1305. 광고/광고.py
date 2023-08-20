import sys
input = sys.stdin.readline

N = int(input())
L = input().rstrip()

def PI(L):
    pi = [0 for i in range(0, len(L))]
    now = 0
    for i in range(1, len(L)):
        while now > 0 and L[i] != L[now]:
            now = pi[now-1]

        if (L[i] == L[now]):
            now += 1
            pi[i] = now
    return N - pi[-1]

res = PI(L)
print(res)
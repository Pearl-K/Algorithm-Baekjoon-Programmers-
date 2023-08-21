import sys
input = sys.stdin.readline

def PI(P):
    pi = [0 for i in range(0, len(P))]

    now = 0
    for i in range(1, len(P)):
        while now > 0 and P[i] != P[now]:
            now = pi[now-1]

        if (P[i] == P[now]):
            now += 1
            pi[i] = now
    return pi

while True:
    s = input().rstrip()
    if s == '.':
        break

    pi = PI(s)
    if len(s) % (len(s)-pi[-1]) != 0:
        print(1)
    else:
        print(len(s)//(len(s)-pi[-1]))
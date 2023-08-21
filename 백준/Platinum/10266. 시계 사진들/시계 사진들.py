import sys
input = sys.stdin.readline

N = int(input())
arr1 = [0]*360000
arr2 = [0]*360000

for i in map(int, input().split()):
    arr1[i] = 1

for i in map(int, input().split()):
    arr2[i] = 1

arr1 += arr1

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

def KMP(T, P):
    pi = PI(P)
    now = 0

    for i in range(0, len(T)):
        while now > 0 and T[i] != P[now]:
            now = pi[now-1]

        if T[i] == P[now]:
            if now == len(P)-1:
                return True
            else:
                now += 1
    return False

print("possible" if KMP(arr1, arr2) else "impossible")

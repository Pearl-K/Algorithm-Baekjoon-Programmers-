import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    res = []

    for i in range(1, n+1):
        for j in range(i, n+1-i):
            if (i+j) == n and (i != j): res.append(str(i) + " " + str(j))
    print("Pairs for "+str(n)+": "+", ".join(res))
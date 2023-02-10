import sys
T = int(sys.stdin.readline())
def find_ak(n, numlist):
    for k in range(1, n):
        a = numlist[0:k].count(2)
        b = numlist[k:].count(2)
        if a == b:
            return k
    return -1

for i in range(T):
    n = int(sys.stdin.readline())
    n_list = list(map(int, sys.stdin.readline().split()))
    result = find_ak(n, n_list)
    print(result)
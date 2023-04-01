import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def binomial(n, k):
    arr = [[0 for x in range(k+1)] for y in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    return arr[n][k]

print(binomial(N, K)%10007)
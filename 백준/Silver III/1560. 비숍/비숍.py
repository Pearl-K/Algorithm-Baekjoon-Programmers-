import sys
input = sys.stdin.readline
N = int(input())
print(N if N <= 2 else 2*N-2)
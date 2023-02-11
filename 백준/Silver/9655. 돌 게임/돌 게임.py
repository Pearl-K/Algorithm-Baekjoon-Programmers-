import sys
input = sys.stdin.readline
N = int(input())
dp = [0, 1, 0, 3]

if (N//3) % 2 == 1: #(N//3)이 홀수
    if N % 3 == 0:
        print('SK')
    elif N % 3 == 1:
        print('CY')
    elif N % 3 == 2:
        print('SK')
else:
    if N % 3 == 0:
        print('CY')
    elif N % 3 == 1:
        print('SK')
    elif N % 3 == 2:
        print('CY')
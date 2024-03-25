import sys
input = sys.stdin.readline
N = int(input())
game = [0, 1, 0, 1, 1] + [0]*(N-4)

if N > 4:
    for i in range(5, N+1):
        if game[i-1] == 0 or game[i-3] == 0 or game[i-4] == 0:
            game[i] = 1

print('SK' if game[N]== 1 else 'CY')
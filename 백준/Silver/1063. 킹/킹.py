import sys
input = sys.stdin.readline
K, S, N = input().split()
k = list(map(int, [ord(K[0]) - 64, K[1]]))
s = list(map(int, [ord(S[0]) - 64, S[1]]))

dxdy = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

for _ in range(int(N)):
    now = input().rstrip() #현재 움직임
    nx = k[0] + dxdy[now][0]
    ny = k[1] + dxdy[now][1]

    if 0 < nx <= 8 and 0 < ny <= 8:
        if nx == s[0] and ny == s[1]:
            # stone
            sx = s[0] + dxdy[now][0]
            sy = s[1] + dxdy[now][1]

            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx, ny]
                s = [sx, sy]
        else:
            k = [nx, ny]

print(chr(k[0] + 64) + str(k[1]))
print(chr(s[0] + 64) + str(s[1]))
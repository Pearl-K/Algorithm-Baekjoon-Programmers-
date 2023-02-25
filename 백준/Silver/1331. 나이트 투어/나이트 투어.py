import sys
pos = sys.stdin.readline().rstrip()
alpha = [0, 'A', 'B', 'C', 'D', 'E', 'F']
visited = []
start_x, start_y = alpha.index(pos[0]), int(pos[1])
X,  Y = start_x, start_y
cnt = 0
for i in range(35):
    pos = sys.stdin.readline().rstrip()
    x, y = alpha.index(pos[0]), int(pos[1])

    if abs(start_x - x) == 2 and abs(start_y - y) == 1:
        if (x, y) not in visited:
            visited.append((x, y))
            start_x, start_y = x, y
        else:
            cnt = 1
    elif abs(start_x - x) == 1 and abs(start_y - y) == 2:
        if (x, y) not in visited:
            visited.append((x, y))
            start_x, start_y = x, y
        else:
            cnt = 1
    else:
        cnt = 1

if cnt == 0 and abs(X-start_x) == 2 and abs(Y-start_y) == 1:
    print('Valid')
elif cnt == 0 and abs(X-start_x) == 1 and abs(Y-start_y) == 2:
    print('Valid')
else:
    print('Invalid')
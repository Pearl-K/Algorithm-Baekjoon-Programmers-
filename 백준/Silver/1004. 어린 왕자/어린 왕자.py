import sys
T = int(sys.stdin.readline())

for i in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    cnt1 = 0
    cnt2 = 0

    for j in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        if (x1-cx)**2 + (y1-cy)**2 <= r**2 and (x2-cx)**2 + (y2-cy)**2 <= r**2:
            # 둘다 한 원 안에 있을 때는 cnt 안세도 됨
            continue
        elif (x2-cx)**2 + (y2-cy)**2 <= r**2:
            cnt2 +=1
        elif (x1-cx)**2 + (y1-cy)**2 <= r**2:
            cnt1 +=1
        else:
            continue
    print(cnt1 + cnt2)
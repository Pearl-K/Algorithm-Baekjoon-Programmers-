import sys
input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    sx, sy, ex, ey, w = map(int, input().split())
    arr.append((w, sx, sy, ex, ey))
arr.sort() # weight 작은 순으로 최소한의 내공 소모

#CCW 사용해서 교차 파악하기?!
def CCW(x1, y1, x2, y2, x3, y3):
    res = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    if res == 0:
        return 0
    elif res < 0:
        return -1
    elif res > 0:
        return 1

def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    ab = CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4)
    cd = CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2)

    if ab == 0 and cd == 0: #swap해서 봐야하는 경우
        if x1 + y1 > x2 + y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if x3 + y3 > x4 + y4:
            x3, y3, x4, y4 = x4, y4, x3, y3

        return x1 + y1 <= x4 + y4 and x3 + y3 <= x2 + y2
    return ab <= 0 and cd <= 0

res = 0
for i in range(n):
    cnt = 1
    for j in range(i+1, n):
        x1, y1, x2, y2 = arr[i][1], arr[i][2], arr[i][3], arr[i][4]
        x3, y3, x4, y4 = arr[j][1], arr[j][2], arr[j][3], arr[j][4]

        if cross(x1, y1, x2, y2, x3, y3, x4, y4):
            cnt += 1
    res += arr[i][0]*cnt
print(res)

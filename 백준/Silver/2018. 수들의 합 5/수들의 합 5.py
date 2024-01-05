import sys
input = sys.stdin.readline

n = int(input())
# 메모리 제한 때문에 배열을 쓰는게 아니라 그냥 수 더하기.빼기 사용
l, r, cnt, sum = 1, 1, 0, 1

while (l <= n) and (r <= n) and (l <= r):
    if sum == n:
        cnt += 1
        sum -= l
        l += 1
    elif sum < n:
        r += 1
        sum += r
    else:
        sum -= l
        l += 1
print(cnt)
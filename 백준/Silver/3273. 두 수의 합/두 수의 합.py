import sys
input = sys.stdin.readline
N = int(input())
a_list = list(map(int, input().split()))
a_list.sort()
X = int(input())
cnt, start, end = 0, 0, N-1

while start < end:
    now = a_list[start] + a_list[end]
    if now < X:
        start += 1
        continue
    if now == X:
        cnt += 1
        start += 1
    else:
        end -= 1

print(cnt)
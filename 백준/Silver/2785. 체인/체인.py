import sys
input = sys.stdin.readline

n = int(input())
ch = sorted(list(map(int, input().split())))
ch.sort()
now, res = len(ch), 0

for i in ch:
    if now <=1:
        break
    if i >= now-1:
        res += now-1
        break
    elif i == 1:
        now -=2
        res +=1
    else:
        for j in range(i-1):
            now -=1
            res +=1
        now -= 2
        res += 1
print(res)
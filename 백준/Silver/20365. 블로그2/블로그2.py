import sys
input = sys.stdin.readline
n = int(input())
color = input().rstrip()
cntB, cntR = 0, 0

if color[0] == 'B':
    cntB += 1
else:
    cntR += 1

for i in range(n-1):
    if color[i] != color[i+1]:
        if color[i+1] == 'B':
            cntB += 1
        else:
            cntR += 1
print(min(cntB, cntR)+1)

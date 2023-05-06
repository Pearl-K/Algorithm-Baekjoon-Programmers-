import sys
input = sys.stdin.readline
S = input().rstrip()
zero = list(S.split('0'))
one = list(S.split('1'))
zcnt, ocnt = 0, 0

for i in zero:
    if i != '':
        zcnt += 1
for i in one:
    if i != '':
        ocnt += 1
print(min(zcnt, ocnt))
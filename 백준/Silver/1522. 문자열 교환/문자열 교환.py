import sys
input = sys.stdin.readline
line = input().strip()
SIZE = len(line)
acnt = line.count('a')
bcnt = line.count('b')

if bcnt == 0:
    print(0)
    sys.exit()

line += line[:acnt-1]
win_b_cnt = line[:acnt].count('b')
res = win_b_cnt

for i in range(1, SIZE):
    if line[i-1] == 'b':
        win_b_cnt -= 1
    if line[i+acnt-1] == 'b':
        win_b_cnt += 1
    res = min(res, win_b_cnt)
print(res)
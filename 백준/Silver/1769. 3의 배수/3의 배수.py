import sys
input = sys.stdin.readline
X = input().rstrip()
num = X
cnt = 0

while int(num) >= 10:
    tmp = 0
    cnt += 1
    for i in num:
        tmp += int(i)

    num = str(tmp)

print(cnt)
print('YES' if int(num)%3 == 0 else 'NO')


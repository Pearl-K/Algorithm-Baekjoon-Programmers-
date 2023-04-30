import sys
input = sys.stdin.readline
N = int(input())
num = ['0']

for i in range(666, 2700000):
    if '666' not in str(i):
        continue
    else:
        num.append(str(i))
print(num[N])
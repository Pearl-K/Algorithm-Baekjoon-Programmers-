import sys
input = sys.stdin.readline
w = input().rstrip()
m = ['a', 'e', 'i', 'o', 'u']
cnt = 0

for i in range(len(w)):
    if w[i] in m:
        cnt += 1
print(cnt)
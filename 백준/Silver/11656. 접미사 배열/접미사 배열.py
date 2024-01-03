import sys
input = sys.stdin.readline
s = input().rstrip()
len_s = len(s)
dic = []

for i in range(len_s):
    dic.append(s[i:])

dic.sort()
print(*dic, sep='\n')

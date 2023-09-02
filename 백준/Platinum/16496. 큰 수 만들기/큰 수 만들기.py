import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(str, input().split()))
arr.sort(key=lambda x:x*11, reverse=True)
res = ''
for i in arr:
    res += i
    
if res == '0'*len(res): print(0)
else: print(res)
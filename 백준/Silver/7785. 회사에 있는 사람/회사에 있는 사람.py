import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for i in range(n):
    name, state = input().rstrip().split()
    dic[name] = state
    if state == "leave":
        del dic[name]

d = sorted(dic.items(), reverse=True)
dic = dict(d)
for k in dic.keys():
    print(k)
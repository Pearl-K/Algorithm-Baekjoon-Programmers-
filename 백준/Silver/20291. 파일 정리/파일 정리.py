N = int(input())
dict = {}
for i in range(N):
    a, b = map(str, input().split('.'))
    if b in dict:
        dict[b] += 1
    else:
        dict[b] = 1

res = list(dict.items())
res.sort(key=lambda x:x[0])

for i in range(len(res)):
    print(res[i][0], res[i][1])
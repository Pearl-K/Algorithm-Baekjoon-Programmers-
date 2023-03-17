N = int(input())
dict = []
for i in range(N):
    x = input()
    dict.append(x)
dict.sort(key=len)
cnt, res = 0, 0

for i in range(N):
    cnt = False
    for j in range(i+1, N):
        if dict[i] == dict[j][0:len(dict[i])]:
            cnt = True
            break

    if not cnt:
        res += 1
print(res)
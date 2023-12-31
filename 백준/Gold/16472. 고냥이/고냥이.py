import sys
input = sys.stdin.readline
n = int(input())
nyang = input().rstrip()
nyang = list(nyang)

len_n = len(nyang)
cnt = set(nyang[0])
s, e = 0, 0
res, now_l = 0, 1 #현재 길이, default 한글자니까 1

while s < len_n-1 and e < len_n-1:
    if len(cnt) > n:
        s += 1
        now_l -= 1
        res = max(res, now_l)
        cnt = set(nyang[s:e+1])
    else:
        e += 1
        now_l += 1
        cnt.add(nyang[e])

if len(cnt) > n:
    res = max(res, now_l-1) #마지막 빠져나왔을 때 체크?
else:
    res = max(res, now_l)
print(res)
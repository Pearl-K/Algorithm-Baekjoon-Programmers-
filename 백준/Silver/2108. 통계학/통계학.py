import sys
from collections import Counter

N = int(sys.stdin.readline())
num = []

for i in range(N):
    n = int(sys.stdin.readline())
    num.append(n)
#산술평균
print(round(sum(num)/len(num)))
#중앙값
num.sort()
print(num[N//2])
#최빈값
cnt = Counter(num).most_common(2)
if len(num) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
#범위
print(max(num) - min(num))
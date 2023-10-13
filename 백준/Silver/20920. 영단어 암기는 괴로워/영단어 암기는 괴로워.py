import sys
input = sys.stdin.readline
n, m = map(int, input().split())
word = dict()
cnt = set()
res = []

for i in range(n):
    w = input().rstrip()
    if len(w) < m:
        continue
    now = len(cnt)
    cnt.add(w)
    plus = len(cnt)

    if now == plus:
        word[w] += 1
    else:
        word[w] = 1

for key, value in word.items():
    res.append([value, len(key), key])

res.sort(key=lambda x:(-x[0], -x[1], x[2]))
for i in res:
    print(i[2])
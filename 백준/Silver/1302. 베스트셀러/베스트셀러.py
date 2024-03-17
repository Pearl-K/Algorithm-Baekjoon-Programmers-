import sys
input = sys.stdin.readline
N = int(input())
book = set()
res = []
for _ in range(N):
    a = input().rstrip()
    now = len(book)
    book.add(a)
    tmp = len(book)

    if now != tmp:
        res.append([a, 1])
    else:
        for i in res:
            if i[0] == a:
                i[1] += 1

res.sort(key=lambda x:(-x[1], x[0]))
print(res[0][0])
import sys
input = sys.stdin.readline
w = input().rstrip()
wl = len(w)
res = []

for i in range(1, wl):
    for j in range(i+1, wl):
        one = ''.join(reversed(w[:i]))
        two = ''.join(reversed(w[i:j]))
        thr = ''.join(reversed(w[j:]))
        res.append(one+two+thr)
res.sort()
print(res[0])
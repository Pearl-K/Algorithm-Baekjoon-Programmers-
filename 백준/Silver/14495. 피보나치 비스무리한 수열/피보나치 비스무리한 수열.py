import sys
n = int(sys.stdin.readline())
f = [0, 1, 1, 1]
for i in range(4, 117):
    f.append(f[i-1]+f[i-3])
print(f[n])
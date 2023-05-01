import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

if abs(w-x) > x:
    a = x
else:
    a = w-x
if abs(h-y) > y:
    b = y
else:
    b = h-y
print(min(a, b))
import sys
input = sys.stdin.readline
def NewRound(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)
n = int(input())
if n:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    new = NewRound(n * 0.15)
    print(NewRound(sum(arr[new:-new] if new else arr) / (n - 2 * new)))
else:
    print(0)
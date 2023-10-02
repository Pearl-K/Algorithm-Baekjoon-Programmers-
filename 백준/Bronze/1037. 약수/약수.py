import sys
input = sys.stdin.readline
n = int(input())

if n == 1:
	factor = int(input())
	print(factor**2)
else:
	arr = list(map(int, input().split()))
	arr.sort()
	print(arr[0]*arr[-1])
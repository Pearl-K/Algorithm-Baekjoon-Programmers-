import sys
input = sys.stdin.readline
one = list(map(int, input().split()))
two = list(map(int, input().split()))
print(max(sum(one), sum(two)))
import sys
input = sys.stdin.readline
N = int(input())
account = list(map(int, input().split()))
J = int(input())
C = int(input())

res = account[0] + (account[0]*J*C)/sum(account)
print(res)
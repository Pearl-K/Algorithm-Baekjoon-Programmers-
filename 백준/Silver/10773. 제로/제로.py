import sys

num = int(input())
stack_list = []

for i in range (num):
  a = int(sys.stdin.readline())
  if a == 0:
    stack_list.pop()
  else :
    stack_list.append(a)

print (sum(stack_list))

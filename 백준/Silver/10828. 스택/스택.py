import sys
n = int(sys.stdin.readline())

stack = []

for i in range (n):
  command = sys.stdin.readline().split() #명령어 받기

  if command[0] == 'push':
    stack.append(command[1])
  elif command[0] == 'pop':
    if len(stack) == 0:
      print(-1) #스택이 비었을 때 -1 출력
    else:
      print(stack.pop())
  elif command[0] == 'empty':
    if len(stack) ==0:
      print(1)
    else:
      print(0)
  elif command[0] == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
  elif command[0] == 'size':
    print(len(stack))
import sys
#큐 문제를 스택으로 구현해보는 미친짓을 하겠습니다.

N = int(sys.stdin.readline())
stack = []
for i in range(N):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if stack:
            print(stack.pop(0))
        else:
            print('-1')

    elif command[0] == 'size':
        if stack:
            print(len(stack))
        else:
            print('0')

    elif command[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')

    elif command[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print('-1')

    else: #back의 경우
        if stack:
            n = len(stack)
            print(stack[n-1])
        else:
            print('-1')


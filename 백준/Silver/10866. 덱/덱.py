import sys
from collections import deque

n = int(sys.stdin.readline())

deque = deque() #덱 선언하는게 중요하다!!

for i in range(n):
    command = sys.stdin.readline().split()
    #split으로 받아서 command[0]에는 명령어, command[1]에는 정수 읽어옴

    if command[0] == 'push_front':
        deque.appendleft(command[1])

    elif command[0] == 'push_back':
        deque.append(command[1])

    elif command[0] == 'pop_front':
        if deque:
            print(deque.popleft())
        else:
            print('-1')
    elif command[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print('-1')

    elif command[0] == 'size':
        print(len(deque))

    elif command[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)

    elif command[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print('-1')
    elif command[0] == 'back':
        if deque:
            print(deque[len(deque)-1])
        else:
            print('-1')
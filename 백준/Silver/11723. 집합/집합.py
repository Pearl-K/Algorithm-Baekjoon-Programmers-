import sys
M = int(sys.stdin.readline())
S = []
for i in range(M):
    command = list(sys.stdin.readline().split())

    if command[0] == 'add':
        if int(command[1]) not in S:
            S.append(int(command[1]))
    elif command[0] == 'remove':
        if int(command[1]) in S:
            S.remove(int(command[1]))
    elif command[0] == 'check':
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            S.append(int(command[1]))
    elif command[0] == 'all':
        S = [i for i in range(1, 21)]
    elif command[0] == 'empty':
        S = []
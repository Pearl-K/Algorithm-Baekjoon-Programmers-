import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    stack1 = []
    stack2 = []
    pw = input().rstrip()
    for j in range(len(pw)):
        if pw[j] == '<':
            if stack1:
                stack2.append(stack1.pop())
        elif pw[j] =='>':
            if stack2:
                stack1.append(stack2.pop())
        elif pw[j] =='-':
            if stack1:
                stack1.pop()
        else:
            stack1.append(pw[j])
    print(''.join(stack1)+''.join(reversed(stack2)))
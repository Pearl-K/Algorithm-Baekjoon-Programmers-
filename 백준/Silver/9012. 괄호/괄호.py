import sys

num = int(input())

for i in range (num):
    stack = []
    a = input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: #스택에 괄호 안들어가 있는 경우 NO 출력
                print("NO")
                break
    else: #break로 끊기지 않은 경우
        if not stack: #중간에 끊기지 않고, 스택이 비어있으면 괄호 맞음
            print("YES")
        else: #스택이 비어있지 않다면 괄호 안맞는 것임
            print("NO")

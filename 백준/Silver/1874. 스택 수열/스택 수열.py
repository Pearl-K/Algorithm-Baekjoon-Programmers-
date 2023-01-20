import sys

count = 1
temp = True
stack = []
command_result = []

n = int(input())


for i in range (n):
    element = int(sys.stdin.readline())

    while count <= element : #읽어온 element 까지 스택에 넣기
        stack.append(count)
        command_result.append('+')
        count += 1

    if stack[-1] == element:
            stack.pop()
            command_result.append('-')

    else:
        temp = False
        
                  
if temp == False:
    print("NO")
else:
    for i in command_result:
        print(i)
import sys
test = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
stack = []
length = len(bomb)
for i in test:
    stack.append(i)
    if i == bomb[-1] and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

result =''.join(stack)

if result:
    print(result)
else:
    print("FRULA")
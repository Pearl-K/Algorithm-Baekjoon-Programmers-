import sys
N = int(sys.stdin.readline())
stack = [] #(height, count) 2차원 배열로 생각할 것
lines = [0 for l in range(N)] #기다리는 사람 목록
result = 0

for i in range(N):
    lines[i] = int(sys.stdin.readline())

for p in lines:
    while stack and stack[-1][0] < p: #stack top 값보다 p 키가 클 때
        result +=stack.pop()[1]

    if not stack: #stack 비어있을 때 해당 키 append하고 continue
        stack.append((p, 1))
        continue

    if stack[-1][0] == p: #stack 끝 값이 p 키와 같을 때
        count = stack.pop()[1] #동일인 얼마나 있는지 count한 변수를 꺼냄
        result += count
        if stack: result +=1
        stack.append((p, count+1))

    else:
        stack.append((p, 1))
        result +=1

print(result)
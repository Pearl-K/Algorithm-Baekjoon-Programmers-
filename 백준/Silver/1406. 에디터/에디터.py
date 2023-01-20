import sys

st1 = list(sys.stdin.readline().rstrip()) #rstirp: 오른쪽 공백 제거
st2 = []
N = int(sys.stdin.readline())
for i in range(N):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())

    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif command[0]== "B":
        if st1:
            st1.pop()

    else: #P '문자' 나오는 커맨드
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))
import sys
board = sys.stdin.readline().rstrip().split('.')
result = ''
for i in board:
    if i == '':
        result += '.'
    else: #X가 들어있을 때
        xnum = len(i) #x의 개수
        if xnum % 2 != 0:
            print(-1)
            sys.exit()
        elif xnum == 2:
            result += 'BB'
        else: #xnum >= 4이상의 짝수
            result += 'AAAA'*(xnum//4)
            result += 'BB'*(xnum%4//2)
        result += '.'
print(result[:-1])
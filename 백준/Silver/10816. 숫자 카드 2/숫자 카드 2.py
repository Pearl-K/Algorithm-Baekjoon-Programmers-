import sys

N = int(sys.stdin.readline())
s_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
result = {}# dictionary 선언

#기존 s_list의 숫자카드, 개수를 result 딕셔너리에 담기
for i in s_list:
    if i in result:
        result[i] +=1
    else:
        result[i] = 1

for i in m_list:
    if i in result:
        print(result[i], end=' ')
    else:
        print(0, end=' ')
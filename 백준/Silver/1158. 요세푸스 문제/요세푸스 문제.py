from collections import deque
n, k = map(int, input().split())

dq = deque() #요세푸스 순열을 풀 때 사용할 덱 선언
result = [] #결과 넣을 리스트 초기화

for i in range(n):
    dq.append(i+1)

while dq: #dq에서 모든 원소가 빠져나갈 때 까지 반복한다.
    for i in range(k-1):
        dq.append(dq.popleft()) #해당 원소가 올 때 까지, 앞 원소를 빼서 뒤에 집어넣기
    result.append(dq.popleft()) #해당 원소 차례에 result로 빼서 넣어준다.

print('<', end='')
for i in range(n):
    if i == n-1:
        print(result[i], end='')
    else:
        print(result[i], end=', ')
print('>', end='')

#복습 용으로 예전 문제 참고 안하고 다시 풀어봄
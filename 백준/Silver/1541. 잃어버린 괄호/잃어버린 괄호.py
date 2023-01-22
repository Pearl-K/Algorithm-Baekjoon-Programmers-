import sys
equ = input().split('-') #마이너스로 리스트 인덱스 구분
count =0 #답(합) 카운트

for i in equ[0].split('+'): #equation[0] 맨 처음 칸에 +가 있는 원소 split
    count += int(i) 
for i in equ[1:]: #남은 칸에 +있는 만큼 스플릿해서 다 빼주기 => 최소값 구하기
    for j in i.split('+'):
        count -=int(j)

print(count)
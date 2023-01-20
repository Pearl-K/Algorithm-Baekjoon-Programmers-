import sys
N = int(sys.stdin.readline())
c_list = [0 for i in range(N)] #컨퍼런스(회의) 시간을 담은 리스트
for i in range(N):
    c_list[i] = list(map(int, sys.stdin.readline().split()))

#1) sort 속의 정렬 옵션 (key=lambda) 활용법 공부하기
c_list.sort(key=lambda x: x[0])
c_list.sort(key=lambda x: x[1])

count = 1 #맨 처음 회의 열었을 때
end = c_list[0][1]
for j in range(1, N):
    if c_list[j][0] >= end:
        count +=1
        end = c_list[j][1]

print(count)
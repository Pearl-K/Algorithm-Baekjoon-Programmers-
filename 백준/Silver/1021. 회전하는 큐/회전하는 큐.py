import sys
from collections import deque
#회전, 순환하는 deque 구상
N, M = map(int, sys.stdin.readline().split())
take = list(map(int, sys.stdin.readline().split()))

num = deque([i+1 for i in range(N)])
cnt = 0

# mid를 기준으로 앞 뒤 길이를 비교한 후
# 2번, 3번 연산중에 골라서 최소 횟수 count 해주기
for i in range(M):
    mid = len(num)//2
    if num.index(take[i]) <= mid: #앞에서 수 꺼내고 뒤로 넘기기
        while take[i] != num[0]:
            num.append(num.popleft())
            cnt += 1 #앞에서 수 꺼낸 만큼 카운팅
        num.popleft() # 원래 찾던 수 뽑아내기
    else: #뒤에서 수 꺼내서 앞으로 넘기기
        while take[i] != num[0]:
            num.appendleft(num.pop())
            cnt +=1
        num.popleft()

print(cnt)
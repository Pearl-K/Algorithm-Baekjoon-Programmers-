import sys
input = sys.stdin.readline
N = int(input())
res = 0
#제일 먼저 시작하는 회의를 임의로 회의실 하나에 배정하면
#해당 회의와 겹치는 모든 회의는 무조건 다른 회의실을 써야한다
#빨리 시작하는 회의부터 배치하면서 각 회의실의 마지막 시간과 비교하면서 채워주기
clist = []
for _ in range(N):
    clist.append(list(map(int, input().split())))

clist.sort(key=lambda x:x[0])
#print(clist)
end_t = [0]*N

for i in range(N):
    if i == 0:
        end_t[i] = clist[i][1]
    else:
        for j in range(i+1):
            if end_t[j] <= clist[i][0]:
                end_t[j] = clist[i][1]
                break
            else:
                continue
for t in end_t:
    if t != 0:
        res += 1
print(res)
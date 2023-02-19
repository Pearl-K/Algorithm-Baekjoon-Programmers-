import sys
#각 세로줄 마다 최빈값을 설정하면 됨
N, M = map(int, sys.stdin.readline().split())
dna = []
result_s = ''
result_n = 0
for i in range(N):
    dna.append(sys.stdin.readline().rstrip())

for i in range(M):
    cnt = {}
    for k in range(N):
        if str(dna[k][i]) in cnt:
            cnt[str(dna[k][i])] += 1
        else:
            cnt[str(dna[k][i])] = 1
    cnt = list(cnt.items())
    cnt.sort(key=lambda x:(-x[1], x[0])) #cnt 같을 때 사전 순 출력
    result_s += str(cnt[0][0])
    for j in range(1, len(cnt)):
        result_n += cnt[j][1]
print(result_s)
print(result_n)
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# LIS의 길이를 출력함
dp = [1]*N
pred = [0]*N

for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            pred[i] = j #이전의 인덱스 j 저장

result = max(dp)
idx = dp.index(result)

print(result)
res = [A[idx]]

prev = pred[idx] #이전의 predecessor 값 저장
for i in range(result-1):
    res.append(A[prev])
    prev = pred[prev]

res.sort()
print(*res, end=' ')
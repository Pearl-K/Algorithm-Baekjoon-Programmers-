N = int(input())
arr = list(map(int, input().split()))
dp = [1]*(N) #default 1

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))
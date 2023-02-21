alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A = input()
B = input()
dp = []
for i in range(len(A)):
    dp.append(alpha[ord(A[i])-65])
    dp.append(alpha[ord(B[i])-65])

result = []
while len(dp) !=2:
    for i in range(1, len(dp)):
        result.append((dp[i] + dp[i-1])%10)
    dp = result
    result = []
print(str(dp[0])+str(dp[1]))
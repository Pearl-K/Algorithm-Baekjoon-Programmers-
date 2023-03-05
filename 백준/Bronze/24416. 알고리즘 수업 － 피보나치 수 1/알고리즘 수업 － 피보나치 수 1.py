n = int(input())
cnt2 = 0
def fib_recursion(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)

def fib_dp(n):
    global cnt2
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        cnt2 += 1
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib_dp(n), cnt2)
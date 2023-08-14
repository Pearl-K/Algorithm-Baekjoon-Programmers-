import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))
fun = [0]*(N+1)
res = [0]*(N+1)

for i in range(1, N+1):
    if i == 1:
        fun[i] = arr[i-1]
    else:
        fun[i] = fun[i-1] + arr[i-1]
        res[i] = res[i-1] + arr[i-1]*fun[i-1]

for i in range(Q):
    S, E = map(int, input().split())
    result = res[E]
    if S == 1:
        print(result)
    else:
        print(result - (fun[E]-fun[S-1])*fun[S-1] -res[S-1])
T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    tmp = arr[-1]*K+1 #max value

    if N > K:
        for j in range(N-K+1):
            tmp = min(tmp, abs(arr[j]-arr[j+K-1]))
    else:
        tmp = abs(arr[-1]-arr[0])
    print("#" + str(i+1) + " " + str(tmp))


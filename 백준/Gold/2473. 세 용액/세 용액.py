import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = sys.maxsize
res_li = [0]*3

for i in range(N-2):
    s, e = i+1, N-1
    while s < e:
        tmp = arr[i] + arr[s] + arr[e]

        if abs(tmp) < res:
            res = abs(tmp)
            res_li[0] = arr[i]
            res_li[1] = arr[s]
            res_li[2] = arr[e]
        if tmp == 0:
            break
        elif tmp < 0:
            s += 1
        else:
            e -= 1
print(*res_li)


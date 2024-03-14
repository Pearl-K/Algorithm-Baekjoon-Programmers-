import sys
input = sys.stdin.readline
N = int(input())
arr = [0] + list(map(int, input().split()))
tmp = [0]*(N+1)

def merge_sort(s, e):
    global res
    if e-s < 1:
        return
    mid = s+(e-s)//2
    merge_sort(s, mid)
    merge_sort(mid+1, e)

    for i in range(s, e+1):
        tmp[i] = arr[i]

    now = s
    idx1 = s
    idx2 = mid+1

    while idx1 <= mid and idx2 <= e:
        if tmp[idx1] > tmp[idx2]:
            arr[now] = tmp[idx2]
            res += idx2-now
            now += 1
            idx2 += 1
        else:
            arr[now] = tmp[idx1]
            now += 1
            idx1 += 1

    while idx1 <= mid:
        arr[now] = tmp[idx1]
        now += 1
        idx1 += 1

    while idx2 <= e:
        arr[now] = tmp[idx2]
        now += 1
        idx2 += 1



res = 0
merge_sort(1, N)
print(res)
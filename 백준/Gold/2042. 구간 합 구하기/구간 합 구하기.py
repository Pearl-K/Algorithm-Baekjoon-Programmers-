import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
sgt = [0]*(n*4)

def init(s, e, idx):
    if s == e:
        sgt[idx] = arr[s-1]
        return sgt[idx]

    mid = (s+e)//2
    sgt[idx] = init(s, mid, idx*2) + init(mid+1, e, idx*2+1)
    return sgt[idx]

def pre_sum(s, e, idx, l, r):
    if s > r or e < l:
        return 0

    if s >= l and e <= r:
        return sgt[idx]

    mid = (s+e)//2
    tmp = pre_sum(s, mid, idx*2, l, r) + pre_sum(mid+1, e, idx*2+1, l, r)
    return tmp

def update(s, e, idx, up_idx, up_data):
    if s > up_idx or e < up_idx:
        return

    sgt[idx] += up_data
    if s == e:
        return

    mid = (s+e)//2
    update(s, mid, idx*2, up_idx, up_data)
    update(mid+1, e, idx*2+1, up_idx, up_data)

init(1, n, 1)
for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1: #update
        diff = c - arr[b-1]
        arr[b-1] = c
        update(1, n, 1, b, diff)
    else: #pre_sum
        print(pre_sum(1, n, 1, b, c))

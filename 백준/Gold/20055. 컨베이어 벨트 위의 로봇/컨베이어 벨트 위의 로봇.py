import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
arr = deque(list(map(int, input().split())))

def findRes(N, K, A):
    step = 0
    belt = deque([False] * N)

    while True:
        step += 1
        arr.rotate(1)
        belt.rotate(1)
        belt[N-1] = False
        
        for i in range(N-2, -1, -1):
            if belt[i] and not belt[i+1] and arr[i+1] > 0:
                belt[i], belt[i+1] = False, True
                arr[i+1] -= 1
                
        belt[N-1] = False
     
        if arr[0] > 0:
            belt[0] = True
            arr[0] -= 1

        if arr.count(0) >= K:
            break
    return step

res = findRes(N, K, arr)
print(res)
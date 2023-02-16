import sys
A, B = sys.stdin.readline().split()
if len(A) == len(B):
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1
    print(cnt)
else: #A 길이가 더 짧을 경우
    count = []
    for i in range(len(B)-len(A) + 1):
        a = 0
        for j in range(len(A)):
            if A[j] != B[i+j]:
                a += 1
        count.append(a)
    print(min(count))
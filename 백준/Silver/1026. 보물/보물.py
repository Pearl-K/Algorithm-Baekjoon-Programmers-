import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# b 배열의 크고 작음을 판단하고, a 리스트 원소 인덱스를 그에 맞게 변환
new_a = [0 for i in range(N)] #재배열 할 A를 만듬

count = 0
for i in range(N):
    count += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print (count)
import sys
N, M = map(int, sys.stdin.readline().split())
pack = []
one = []
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    pack.append(a)
    one.append(b)
pack.sort()
one.sort()
O = min(one)
P = min(pack)

#1. 모두 낱개 / #2. 모두 패키지 / 3. 패키지+낱개 혼합
result = min(O*N, P*(N//6+1), (P*(N//6) + O*(N%6)))
print(result)
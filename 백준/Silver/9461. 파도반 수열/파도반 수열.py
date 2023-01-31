T = int(input())
#P[N] = P[N-3] + P[N-2]인 피보나치 수열
#재귀함수는 시간초과, 리스트로 풀기

p = [0 for i in range(101)]
p[1], p[2], p[3] = 1, 1, 1

for i in range(4, 101):
    p[i] = p[i-3] + p[i-2]

for i in range(T):
    N = int(input())
    print(p[N])

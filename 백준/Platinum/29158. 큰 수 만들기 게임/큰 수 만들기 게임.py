import sys
input = sys.stdin.readline

prime = [1 for i in range(10**6+1)]
prime[0], prime[1] = 0, 0

now = 2
while now * now <= 10**6:
    if prime[now]:
        for i in range(2*now, 10**6+1, now):
            prime[i] = 0
    now += 1

N = int(input())
N_factors = []
N_cp = N

if N == 2:
    print(3)
    sys.exit()

now = 2
while now * now <= N_cp:
    if prime[now]:
        while N_cp%now == 0:
            N_factors.append(str(now))
            N_cp //= now
    now += 1
if N_cp != 1:
    N_factors.append(str(N_cp))

N_factors.sort(key=lambda x:x*13, reverse=True)
N_res = ""
for x in N_factors:
    N_res += x
N_res = int(N_res)

cnt2, cnt3 = 0, 0
start = 1

while start*2 < N:
    start *= 2
    cnt2 += 1

if (start//2)*3 < N and cnt2 > 0:
    start = (start//2)*3
    cnt2 -= 1
    cnt3 += 1
M_res = int("3"*cnt3 + "2"*cnt2)

print(N_res + M_res)
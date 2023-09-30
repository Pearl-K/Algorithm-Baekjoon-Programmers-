import sys
input = sys.stdin.readline
n = int(input()) # 1 <= n <= 4000000
#에라토스테네스 체로 소수 배열 만들고 투 포인터로 누적합 모든 경우의 수 세기
prime = [True]*(n+1)
prime[0], prime[1] = False, False
pre_s =[]

def erat():
    now = 2 # 0과 1은 소수가 아니다

    while now * now <= (n+1):
        for i in range(now, n+1, now):
            if i != now:
                prime[i] = False
        now += 1

    for i in range(n+1):
        if prime[i]:
            if not pre_s:
                pre_s.append(i)
            else:
                pre_s.append(i+pre_s[-1]) #누적합 배열 만들기

erat()
#print(prime)
#print(pre_s)
#투 포인터를 통한 연속합 구간 경우의 수 구하기
start, end, res = -1, 0, 0

while start <= end and end < len(pre_s):
    if start == -1:
        tmp = pre_s[end]
    else:
        tmp = pre_s[end] - pre_s[start]

    if tmp == n:
        res += 1
        end += 1
    elif tmp < n:
        end += 1
    else:
        start += 1
print(res)
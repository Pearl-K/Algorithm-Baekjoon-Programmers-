import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
lights = []
res = 3**N

for now in S:
    if now == "R":
        lights.append(0)
    elif now == "G":
        lights.append(1)
    elif now == "B":
        lights.append(2)



for t in range(3):
    tmp = lights.copy()
    cnt = 0
    
    for i in range(N-2):
        change = (t-tmp[i]) % 3
        cnt += change
        
        for j in range(3):
            tmp[i+j] += change
            tmp[i+j] %= 3
            
    if all (t==n for n in tmp):
        if res > cnt:
            res = cnt
            
if res!=3**N:
    print(res)
else:
    print(-1)
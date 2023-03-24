import sys
M, N = map(int, sys.stdin.readline().split())
num = [i for i in range(M, N+1)]
cnt = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for i in range(len(num)):
    if len(str(num[i])) == 1:
        num[i] = cnt[num[i]]
    if len(str(num[i])) == 2:
        #10의 자리 + 1의 자리 str로 바꿔서 더하기
        num[i] = cnt[num[i]//10] +' '+ cnt[num[i]%10]

num.sort()

for i in range(len(num)):
    if ' ' in num[i]:
        a, b = num[i].split()
        new = str(cnt.index(a)) + str(cnt.index(b))
        num[i] = int(new)
    else:
        num[i] = cnt.index(num[i])

a = len(num)//10 
b = len(num)%10

for i in range(a):
    for k in range(10):
        print(num[k+10*i], end =' ')
    print()

for k in range(b):
    print(num[k+10*a], end=' ')
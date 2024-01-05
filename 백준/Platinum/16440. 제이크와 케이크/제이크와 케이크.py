import sys
input = sys.stdin.readline
n = int(input())
cake = input().rstrip()
st, ki = 0, 0

for i in range(n//2):
    if cake[i] == 's':
        st += 1
    else:
        ki += 1

def sliding_window(st, ki):
    s, e = 0, n//2-1

    while True:
        if st == ki:
            if s == 0:
                print(1)
                cut = [e+1]
                return cut
            else:
                print(2)
                cut = [s, e+1]
                cut.sort() #시작과 끝의 인덱스 순서 오름차순 만들기
                return cut

        if cake[s] == 's': #start 포인터 옮기기
            st -= 1
        else:
            ki -= 1
        s += 1

        e += 1 #end 포인터 옮기기
        if e == n:
            e = 0 #앞으로 다시 돌아감
        if cake[e] == 's':
            st += 1
        else:
            ki += 1

cut = sliding_window(st, ki)
print(*cut)
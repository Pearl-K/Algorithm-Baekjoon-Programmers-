N = int(input())

def hanoi(n, start, tmp, end):

    if n == 1:
        print(start, end)
        return 0
    else:
        hanoi(n-1, start, end, tmp)
        print(start, end)
        hanoi(n-1, tmp, start, end)

print(2**N -1) #하노이탑의 실행 횟수를 함수로 구하면 2^n -1이다.
hanoi(N, 1, 2, 3)
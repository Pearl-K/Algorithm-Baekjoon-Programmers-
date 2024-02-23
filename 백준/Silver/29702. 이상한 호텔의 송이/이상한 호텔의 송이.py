import sys
input = sys.stdin.readline
sys.setrecursionlimit(100)

#층수 => 이진수의 length, 방번호
#자기 부모 찾기 => 자기 마지막 비트 하나 없애면 됨 (>>)

def print_path(num):
    if num == 1:
        print(1000000000000000001)
        return

    b_n = bin(num)[2:]

    F = len(b_n)
    room = abs(2**(F-1) - num) + 1
    #print(F, room)
    print(str(F)+'0'*(18-len(str(room)))+str(room))
    print_path(num >> 1)


T = int(input())
for _ in range(T):
    N = int(input())
    print_path(N)

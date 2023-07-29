#23.07.29 시작 시간 9:10 PM, 완료 시간 9:37 PM
import sys
input = sys.stdin.readline

#모든 경우의 수 안에서 순열로 해결 가능
N = int(input())

import itertools

num_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
HW = itertools.permutations(num_1, 2)
HW = list(HW)

for i in range(len(HW)):
    num_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    h = HW[i][0]
    w = HW[i][1]

    num_2.remove(h)
    num_2.remove(w)

    left = itertools.permutations(num_2, 5)
    left = list(left)

    for j in range(len(left)):
        res = 0
        d = left[j][0]
        e = left[j][1]
        l = left[j][2]
        o = left[j][3]
        r = left[j][4]

        res += h*(10**4) + e*(10**3) + l*(10**2) + l*(10**1) + o
        res += w*(10**4) + o*(10**3) + r*(10**2) + l*(10**1) + d

        if res == N:
            print("  "+str(h)+str(e)+str(l)+str(l)+str(o))
            print("+ "+str(w)+str(o)+str(r)+str(l)+str(d))
            print("-------")
            if len(str(N)) == 5: #자릿수에 따른 공백 출력 다르게 ^^
                print("  "+str(N))
            else:
                print(" "+str(N))
            sys.exit()

print("No Answer")
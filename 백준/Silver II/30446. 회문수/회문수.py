import sys
input = sys.stdin.readline

def solve(N):
    # 한자리 ~ 5자리의 회문수까지.?
    arr = [0, 9, 9, 90, 90, 900, 900, 9000, 9000, 90000, 90000]
    res = 0
    len_n = len(N)

    if len_n == 1:
        print(int(N))
    else:
        for i in range(len_n):
            res += arr[i]
        # 101 이면 10 1
        # 1001 이면 10 01
        # 44444 이면 100 01 이런식으로 카운트

        if (len_n % 2) != 0:  # 홀짝 나눠서
            tmp = 10 ** (len_n // 2)
            while True:
                s = str(tmp)
                e = str(tmp)[:-1][::-1]
                pal = s + e

                if int(pal) <= int(N):
                    tmp += 1
                    res += 1
                    #print(s, e, pal)
                else:
                    break
            print(res)
            sys.exit()
        else:
            tmp = 10 ** (len_n // 2-1)
            while True:
                s = str(tmp)
                e = str(tmp)[::-1]
                pal = s + e

                if int(pal) <= int(N):
                    tmp += 1
                    res += 1
                    #print(s, e, pal)
                else:
                    break
            print(res)
            sys.exit()

N = int(input().rstrip())
solve(str(N))
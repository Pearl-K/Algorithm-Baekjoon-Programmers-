while True:
    try:
        n = int(input())
        result, cnt = 1, 0
        while (result % n) != 0:
            cnt += 1
            result += 10 ** cnt
        print(len(str(result)))
    except EOFError:
        break
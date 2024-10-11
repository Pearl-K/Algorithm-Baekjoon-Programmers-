T = int(input())
for i in range(1, T+1):
    n = int(input())
    res = ""
    if n <= 25:
        res += "World Finals"
    elif n <= 1000:
        res += "Round 3"
    elif n <= 4500:
        res += "Round 2"
    else:
        res += "Round 1"
    print("Case #"+str(i)+": " +res)
import sys
N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
cal_list = [0]
for i in range(N):
    d = int(sys.stdin.readline())
    cal_list.append(d)
cal_list.sort(reverse=True)

result = C/A

for k in range(1, len(cal_list)+1):
    calo = C + sum(cal_list[0:k])
    price = A + (B*k)

    if calo/price > result:
        result = calo / price
    else:
        break
print(int(result))
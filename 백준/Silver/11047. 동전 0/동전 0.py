import sys
n, k = map(int, sys.stdin.readline().split())
price = [0 for i in range(n)]
for i in range(n):
    price[i] = int(sys.stdin.readline())

def min_amount (a, a_list):
    count = [0 for i in range(len(a_list))]
    for i in range(len(a_list)):
        count[i] += a // a_list[(len(a_list))-i-1]
        a = a - (a_list[(len(a_list))-i-1]*count[i])

    return sum(count)

ans = min_amount(k, price)
print(ans)
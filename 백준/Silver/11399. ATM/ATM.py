import sys
N = int(sys.stdin.readline())
t_list = [0 for i in range(N)]

t_list= list(map(int, input().split()))

def min_sum(some_list):
    some_list.sort()
    count = [0 for i in range(len(some_list))]

    for i in range(len(some_list)):
        if i == 0:
            count[i] = some_list[i]
        else:
            count[i] = count[i-1] + some_list[i]

    return sum(count)

print(min_sum(t_list))
n = int(input())
std = [list(input().split()) for i in range(n)]
std.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(n):
    print(std[i][0])

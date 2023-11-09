x = int(input())
cnt = 1
min_l = 64
sum_l = 64
while x < sum_l:
    min_l //= 2
    if sum_l - min_l >= x:
        sum_l -= min_l
    else:
        cnt += 1
print(cnt)
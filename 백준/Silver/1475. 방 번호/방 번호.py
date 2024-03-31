N = input()
num = [0 for i in range(10)]

for n in N:
    num[int(n)] += 1

max_n = 0
max96 = (num[6] + num[9])//2 + (num[6] + num[9])%2
for i in range(10):
    if i == 6 or i == 9:
        continue
    else:
        max_n = max(max_n, num[i])
print(max(max_n, max96))

import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))

res = 0
new = sorted(arr)

for i in range(n):
    idx_diff = new[i][1]-i
    res = max(res, idx_diff)
print(res+1)
#idx_diff의 최댓값, 정렬된 후 반복문 한 번 더 추가 실행
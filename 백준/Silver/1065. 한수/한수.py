import sys
input = sys.stdin.readline
n = int(input())
cnt = 0

for i in range(1, n+1):
    arr = list(map(int, str(i)))
    if i < 100: #한자리~두자리수는 모두 각 자리가 등차수열임
        cnt += 1
    elif arr[0]-arr[1] == arr[1]-arr[2]:
        cnt += 1

print(cnt)
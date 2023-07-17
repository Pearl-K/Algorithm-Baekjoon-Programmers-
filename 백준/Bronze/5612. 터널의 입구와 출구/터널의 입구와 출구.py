import sys
input = sys.stdin.readline
N = int(input())
car = []
car.append(int(input()))

for i in range(N):
    a, b = map(int, input().split())
    now = car[i] + a-b
    car.append(now)

for i in range(N+1):
    if car[i] < 0:
        print(0)
        sys.exit()
print(max(car))
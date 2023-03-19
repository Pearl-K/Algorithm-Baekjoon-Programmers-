N = int(input())
X = list(map(int, input().split()))

X1 = set(X)
X1 = list(X1)
X1.sort() #내림차순, 자기 index 수가 자기보다 작은 좌표 수

dict = {X1[i]: i for i in range(len(X1))}

for i in X:
    print(dict[i], end=' ')
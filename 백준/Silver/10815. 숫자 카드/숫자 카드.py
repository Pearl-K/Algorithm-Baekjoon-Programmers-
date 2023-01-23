import sys
N = int(input())
haves = list(map(int, sys.stdin.readline().split()))
M = int(input())
cards = list(map(int, sys.stdin.readline().split()))

#딕셔너리 컴프리헨션 사용해서 list to dictionary
dictionary = {i: 0 for i in cards}

for i in range(N):
    if haves[i] in dictionary:
        dictionary[haves[i]] +=1

print(*dictionary.values())
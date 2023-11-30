import sys
input = sys.stdin.readline

move = []
x = [] 
y = [] 
low = []
k = int(input())

for i in range(6):
    dir, dist = map(int, input().split())
    move.append([dir, dist])
    if move[i][0] == 3 or move[i][0] == 4:
        x.append(move[i][1])
    if move[i][0] == 1 or move[i][0] == 2:
        y.append(move[i][1])

for i in range(6):
    if move[i][0] == move[(i+2)%6][0]:
        low.append(move[(i+1)%6][1])
print(((max(x)*max(y))-(low[0]*low[1]))*k)
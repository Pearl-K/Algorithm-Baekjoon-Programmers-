import sys
input = sys.stdin.readline
N = int(input())
dance = set()

for i in range(N):
    name1, name2 = input().split()
    if name1 == 'ChongChong' or name2 == 'ChongChong':
        dance.add(name1)
        dance.add(name2)
    else:
        if name1 in dance:
            dance.add(name2)
        elif name2 in dance:
            dance.add(name1)
print(len(dance))
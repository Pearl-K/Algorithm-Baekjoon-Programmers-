import sys
input = sys.stdin.readline

tree = {}
t = 0

while True:
    a = input().rstrip()

    if not a:
        break
    if a in tree:
        tree[a] += 1
    else:
        tree[a] = 1
    t += 1

tree_list = list(tree.keys())
tree_list.sort()

for k in tree_list:
    print('%s %.4f' %(k, tree[k]/t*100))
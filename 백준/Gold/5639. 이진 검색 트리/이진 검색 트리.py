import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

def PostOrder(start, end):
    if start > end:
        return

    mid = end + 1
    for i in range(start+1, end+1):
        if tree[i] > tree[start]:
            mid = i
            break
    PostOrder(start+1, mid-1)
    PostOrder(mid, end)
    print(tree[start])

PostOrder(0, len(tree)-1)
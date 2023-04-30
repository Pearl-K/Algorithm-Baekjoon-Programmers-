import sys
input = sys.stdin.readline
N = int(input())
tree = {}

for i in range(N):
    root, lf, rt = input().split()
    tree[root] = [lf, rt]

def Pre(root):
    if root != '.':
        print(root, end='')
        Pre(tree[root][0])
        Pre(tree[root][1])

def In(root):
    if root !='.':
        In(tree[root][0])
        print(root, end='')
        In(tree[root][1])

def Post(root):
    if root != '.':
        Post(tree[root][0])
        Post(tree[root][1])
        print(root, end='')

Pre('A')
print()
In('A')
print()
Post('A')
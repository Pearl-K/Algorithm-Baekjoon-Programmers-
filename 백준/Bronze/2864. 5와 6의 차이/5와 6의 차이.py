import sys
input = sys.stdin.readline
A, B = map(str, input().split())

def find_max(A, B):
    if '5' in A:
        A = A.replace('5', '6')
    if '5' in B:
        B = B.replace('5', '6')

    return int(A) + int(B)

def find_min(A, B):
    if '6' in A:
        A = A.replace('6', '5')
    if '6' in B:
        B = B.replace('6', '5')

    return int(A) + int(B)

print(find_min(A, B), find_max(A,B))
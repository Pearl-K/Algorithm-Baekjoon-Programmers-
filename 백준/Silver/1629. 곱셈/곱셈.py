import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def mod_calculator(x, y, z):
    if y == 0:
        return 1
    if y%2 == 0: # y가 짝수
        res = mod_calculator(x, y//2, z)
        return (res * res) % z
    else: #y가 홀수
        res = mod_calculator(x, y-1, z)
        return (x * res) % z

print(mod_calculator(A, B, C))
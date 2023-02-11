import sys
input = sys.stdin.readline
N = int(input())
stack = []
final_score = 0
for i in range(N):
    assign = list(map(int, input().split()))
    if assign[0] == 0:
        if stack:
            stack[-1][1] -= 1
        else:
            continue
    else:
        assign[2] -= 1
        stack.append([assign[1], assign[2]])

    if stack:
        if stack[-1][1] == 0:
            final_score += stack[-1][0]
            stack.pop()
print(final_score)
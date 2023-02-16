import sys
hansoo = sys.stdin.readline().rstrip()
# 가운데를 기준으로 반 자른다고 생각하면
# 왼쪽, 오른쪽 하나 씩 주면 된다.
# 문자열의 문자 개수를 count하고, 모두 짝수 개수 + 홀수 개수 1개
dict = {}
for i in hansoo:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
d1 = sorted(dict.items())
center = []
cnt = 0
for i in range(len(d1)):
    if d1[i][1]%2 != 0:
        center.append(i)
        cnt += 1
result = ''
if cnt <=1:
    for i in range(len(d1)):
        result += d1[i][0]*(d1[i][1]//2)
    rev_result = result[::-1]
    if center:
        result += d1[center[0]][0]
    result += rev_result
    print(result)
else:
    print("I'm Sorry Hansoo")
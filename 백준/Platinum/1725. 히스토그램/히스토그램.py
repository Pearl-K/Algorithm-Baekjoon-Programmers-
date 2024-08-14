import sys
input = sys.stdin.readline

N = int(input())
stick = [int(input()) for _ in range(N)]
st = []
max_area = 0;

for i in range(N):
    while st and stick[st[-1]] > stick[i]:
        height = stick[st.pop()]
        if not st: width = i
        else: width = i - st[-1] - 1

        max_area = max(max_area, height*width)
    st.append(i) #인덱스 넣기

while st:
    height = stick[st.pop()]
    if not st:
        width = N #width가 전체 개수인지 체크
    else:
        width = N - st[-1] - 1
    max_area = max(max_area, height * width)

print(max_area)
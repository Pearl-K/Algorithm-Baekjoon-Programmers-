import sys
input = sys.stdin.readline

cnt = 0
st = []
li = list(input().rstrip())
li_len = len(li)

for i in range(li_len):
    if li[i] =='(':
        st.append('(')
    else:
        if li[i-1] == '(':
            st.pop()
            cnt += len(st)
        else:
            st.pop()
            cnt += 1
print(cnt)

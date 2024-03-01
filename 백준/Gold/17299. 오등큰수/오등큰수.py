import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_v = max(arr)
cnt = [0]*(max_v+1)
res = [-1]*N
st = []

for now in arr:
    cnt[now] += 1

for i in range(N):
    while st and cnt[arr[st[-1]]] < cnt[arr[i]]:
        top = st.pop()
        res[top] = arr[i]
    st.append(i)
print(*res)

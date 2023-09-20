import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
st = []
check = 1

for now in arr:
	st.append(now)
	while st and st[-1] == check: # tmp 스택 하나로 비교
		st.pop()
		check += 1
	if len(st) > 1 and st[-1] > st[-2]:
		print("Sad")
		sys.exit()

if st:
	print("Sad")
else:
    print("Nice")
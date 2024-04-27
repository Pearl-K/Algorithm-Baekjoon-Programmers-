n = int(input())
for i in range(n):
    pw = input()
    if 6 <= len(pw) <= 9:
        print("yes")
    else:
        print("no")
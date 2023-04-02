S = input()
sl = len(S)
substring = []
for i in range(sl):
    for j in range(sl-i):
        substring.append(S[j:j+i+1])

result = set(substring)
result = list(result)
print(len(result))
import sys
N = int(sys.stdin.readline())
dict = []

def digit(numlist):
    result = 0
    for i in numlist:
        if i.isdigit():
            result +=int(i)
    return result

for i in range(N):
    s = sys.stdin.readline().rstrip()
    dict.append(s)
dict.sort(key = lambda x: (len(x), digit(x), x))

for i in dict:
    print(i)
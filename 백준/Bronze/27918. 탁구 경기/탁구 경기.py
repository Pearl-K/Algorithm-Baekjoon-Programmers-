n = int(input())
d, p = 0, 0
for i in range(n):
    a = input()
    
    if a == 'D':
        d += 1
    else:
        p += 1
    if abs(d-p) >= 2:
        break
      
print(str(d)+":"+str(p))
        
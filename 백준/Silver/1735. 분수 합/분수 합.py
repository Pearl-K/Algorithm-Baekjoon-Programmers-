import sys
import math
a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
# 두 분수의 합 구하기
numerator = (a*d) + (c*b)
denominator = b*d
# 기약 분수로 만들기
gcd1 = math.gcd(numerator, denominator)
numerator //=gcd1
denominator //=gcd1
print(numerator, denominator)
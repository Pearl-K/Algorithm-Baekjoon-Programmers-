for i in range(3, 0, -1):
    num = input()
    if num not in ['Fizz', 'Buzz', 'FizzBuzz']: #숫자 들어왔을 때
        nxt = int(num) + i
print('Fizz'*(nxt % 3 == 0) + 'Buzz'*(nxt % 5 == 0) or nxt)
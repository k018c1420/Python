i = int(input('入力＞'))

for x in range(i):
    if (x + 1) % 3 == 0 and (x + 1) % 5 == 0:
        print('FizzBuzz', end=',')
    elif (x + 1) % 3 == 0:
        print('Fizz', end=',')
    elif (x + 1) % 5 == 0:
        print('Buzz', end=',')
    else:
        print((x + 1), end=',')
i = int(input('入力＞'))
charge = 200
add = 0

if i <= 10:
    print(charge, '円')
else:
    add = (i - 10) * 20
    print(charge + add, '円')
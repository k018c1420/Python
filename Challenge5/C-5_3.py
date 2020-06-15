year = int(input('西暦＞'))

if year % 4 == 0 and year % 100 != 0:
    print('うるう年')
else:
    print('平年')
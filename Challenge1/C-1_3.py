i = int(input('月数＞'))
1
if i >= 12:
    y = int(i / 12)
    m = int(i % 12)
    print(y, '年', m, 'ヶ月')
else:
    y = 0
    m = i
    print(y, '年', m, 'ヶ月')

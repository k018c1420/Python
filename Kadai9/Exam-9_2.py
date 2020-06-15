year = int(input('西暦＞'))

if year >= 1896 and (year - 1896) % 4 == 0:    #   追加箇所
    print('開催年です')
else:
    print('開催年ではありません')

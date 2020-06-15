i = int(input('数値＞'))
yakusuu = []

for x in range(i):
    if i % (x + 1) == 0:
        yakusuu.append(x + 1)

if len(yakusuu) == 2:
    print('素数です')
else:
    print('素数ではありません') 
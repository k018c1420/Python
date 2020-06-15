i = int(input('数値＞'))

for x in range(i):
    if i % (x + 1) == 0:
        print((x + 1), end=',')
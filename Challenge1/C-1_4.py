i = int(input('金額＞'))
man = 0
gosen = 0
sen = 0

if i / 10000 != 0:
    man = int(i / 10000)
    i %= 10000
if i / 5000 != 0:
    gosen = int(i / 5000)
    i %= 5000
if i / 1000 != 0:
    sen = int(i / 1000)
    i %= 1000

print('10000円札', man)
print('5000円札', gosen)
print('1000円札', sen)

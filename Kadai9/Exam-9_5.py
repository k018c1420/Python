i = 1
num = []
sum = 0
while i != 0:
    i = int(input('数値＞'))
    num.append(i)

for x in num:
    sum += x

print('合計：',sum)
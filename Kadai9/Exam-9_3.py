height = int(input('身長＞'))
weight = int(input('体重＞'))

bmi = weight / (height / 100 * height / 100)

if bmi >= 25:
    print('肥満')
elif bmi >= 18.5:
    print('標準')
else:
    print('痩せすぎ')
i = int(input('数値＞'))
k = 1

for x in range(1, i + 1, 1):
    k *= x
print(i, 'の階乗：', k)
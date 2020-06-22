def func(i):
    if i > 1:
        return i * func(i - 1)
    return 1
    
i = int(input('数値＞'))
print("階乗：" + str(func(i)))

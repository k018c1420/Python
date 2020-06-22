def func(a, b):
    if a % b == 0:
        return b
    else:
        return func(b, a % b)
    
a = int(input('数値１＞'))
b = int(input('数値２＞'))

print("最大公約数：" + str(func(a, b)))

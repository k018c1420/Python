def func(width, height):
    return width * height / 2
    
t = int(input('上底＞'))
b = int(input('下底＞'))
h = int(input('高さ＞'))
out = func(t + b, h)
print("台形の面積：" + str(out))


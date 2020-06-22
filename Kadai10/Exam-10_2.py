def func(width, height):
    return width * height / 2
    
w = int(input('底辺＞'))
h = int(input('高さ＞'))
out = func(w, h)
print("三角形の面積：" + str(out))


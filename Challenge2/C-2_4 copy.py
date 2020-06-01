i = input('入力＞')
length = len(i)
print(length - len(i.replace(' ', '')) + 1)
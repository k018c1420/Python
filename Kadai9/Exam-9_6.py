i = ''
words = []
while True:
    i = input('単語＞')
    if i in words:
        print('終了')
        print(words)
        break
    else:
        words.append(i)

words = ['しりとり']
while True:
    i = input('答え＞')
    if words[-1][-1] == i[0]:
        if i[-1] == 'ん' or i in words:
            print('あなたの負けです')
            break
        else:
            words.append(i)
    else:
        print('もう一度答えてください')
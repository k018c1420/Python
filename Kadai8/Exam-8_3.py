password = input('入力＞')

if len(password) < 8:    #   追加箇所
    print('短すぎます')    #   追加箇所
elif len(password) >= 13:    #   追加箇所
    print('長すぎます')    #   追加箇所
else:    #   追加箇所
    print('O.K.')    #   追加箇所

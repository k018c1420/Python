i = input('入力＞')
words = ''
count = 0

for value in i:
    if value != ' ' and words == '':
        count+=1
        words += value
    elif value == ' ':
        words = ''

print(count)


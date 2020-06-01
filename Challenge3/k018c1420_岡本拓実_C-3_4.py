i = input('入力＞')
i = i.split('.')
hex = '0123456789ABCDEF'
part = ''
ans = []

for x in range(len(i)):
    if i[x] == '0':
        ans.append('00')
    else:
        i[x] = int(i[x])
        while i[x] > 0:
            j = int(i[x] % 16)
            i[x] = int(i[x] / 16)
            part = hex[j] + part
        ans.append(part)
        part = ''

answer = ':'.join(ans)
print(answer)
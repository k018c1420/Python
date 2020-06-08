i = int(input('入力＞'))
x = []

while i > 0:
    x.append(i % 2)
    i = int(i / 2)

for ans in reversed(x):
    print(ans, end='')
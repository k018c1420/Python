i = input()
i = i.split(' ')

i.sort(reverse=True)

one = i[0] + i[2]
two = i[1] + i[3]

print(int(one) + int(two))

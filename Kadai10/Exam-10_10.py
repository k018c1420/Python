def funcSum(list):
    sum = 0
    for i in list:
        sum += int(i)
    return sum

def funcAve(list):
    return funcSum(list) / len(list)

def funcMax(list):
    temp = 0
    for i in list:
        if temp < int(i):
            temp = int(i)
    return temp
    
i = input('数値＞').split()

print("平均：" + str(funcAve(i)))
print("最大値：" + str(funcMax(i)))



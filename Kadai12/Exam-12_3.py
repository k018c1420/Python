from Dice import Dice
import time

d1 = Dice(6)
d2 = Dice(6)
d3 = Dice(6)

while True:
    list = [d1.roll(), d2.roll(), d3.roll()]

    print(list)

    time.sleep(.3)

    if(list[0] == list[1] and list[1] == list[2]):
        print("当たり！")
        break
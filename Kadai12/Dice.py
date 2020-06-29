import random
list = ['大吉', '中吉', '小吉', '凶', '大凶']

class Dice:

    def __init__(self, num):
        self.num = num

    def roll(self):
        i = random.randint(1, self.num)
        return i
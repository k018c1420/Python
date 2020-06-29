import random
list = ['大吉', '中吉', '小吉', '凶', '大凶']

class Fortune:

    def draw(self):
        i = random.randrange(5)
        print(list[i])
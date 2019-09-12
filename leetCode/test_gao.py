class gaocy:


    def __init__(self, age, height, weight, muscle_quality):
        self.age = age
        self.height = height
        self.weight = weight
        self.muscle_quality = muscle_quality

    def exercise(self):
        self.muscle_quality += 1
    # def eat(self, weight):
    # 	weight += 1


if __name__ == '__main__':
    gao = gaocy(age=23, height= 175, weight = 75, muscle_quality = 0)
    print("gaocy age:{0}; weight:{1}; height:{2}; muscle_quality:{3}".format(gao.age, gao.weight, gao.height, gao.muscle_quality))
    gao.exercise()
    print("gaocy age:{0}; weight:{1}; height:{2}; muscle_quality:{3}".format(gao.age, gao.weight, gao.height, gao.muscle_quality))

    # print(gao.muscle_quality)
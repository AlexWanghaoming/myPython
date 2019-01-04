import test1
import test1
class WorkSalary:

    def __init__(self):
        self.__observers = []
        self.__salary = 4500
        self.msps = Sps(self)
    def getSalary(self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary
        print('Currently salary is:', self.__salary)
        self.notifies()

    def addObserver(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for each in self.__observers:
            each.update(self)




class Observer:
    def update(self, workSalary):
        pass

class EatMode(Observer):
    def update(self, workSalary):
        if workSalary.getSalary()>=5000 and workSalary.getSalary()<6000:
            print("I can eat dinner with Lili")
        elif workSalary.getSalary()>=6000 and workSalary.getSalary()<7000:
            print("I can by a new shoes")

class TravelMode(Observer):
    def update(self, workSalary):
        if workSalary.getSalary()>=7000:
            print("I can travel in Hangzhou!")

"""
Let's test it!
"""

if __name__ == '__main__':
    salary = WorkSalary()
    eatOb = EatMode()
    travOb = TravelMode()

    salary.addObserver(eatOb)
    salary.addObserver(travOb)

    import random
    for _ in range(3):
        salary_AUG = random.choice(range(5000, 8000, 500))
        salary.setSalary(salary_AUG)

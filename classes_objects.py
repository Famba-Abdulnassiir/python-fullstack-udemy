## Almost everything in Python is an object, with its properties and methods.
## A Class is like an object constructor, or a "blueprint" for creating objects

class Lotteryplayer:
    def __init__(self,name):
        self.name = name
        self.numbers = (5,12,10,3,1,21)

        def total(self):
            return sum(self.numbers)

player_one = Lotteryplayer("Famba")
player_two = Lotteryplayer("Vero")
print(player_one.name)

class student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

ann = student("Anna", "BIT")
ann.marks.append(78)
ann.marks.append(70)
print(ann.name, ann.school, ann.marks)

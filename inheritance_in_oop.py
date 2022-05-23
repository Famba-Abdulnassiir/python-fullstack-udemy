from ossaudiodev import SNDCTL_SYNTH_CONTROL


class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school,salary)

## Create object anna from Studnet class then create friend from Anna object   
# this code is before inheritance took place.
 
# anna = Student("Famba", "Alliance High School")
# friend = anna.friend("Elijah")

# print(friend.school)

## Class Working Student inherits all properties of student just pass
## Please note inheritance is not like cloning we they may have some differences.
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

famba = WorkingStudent("Famba","Alliance High School", 23.00)
print(famba.salary)

friend = WorkingStudent.friend(famba,"Elijah", 1000.00)
print(friend.name)
print(friend.salary)

##Lists are [] a collection of related data in it. lists are mutable or can be changed at any time.

grades =[77,80,58,100,107]

##This is the same as a list but unlike list tuples are immutable
tuple_grades =(77,80,58,100,107) #immutable no changes can be done to it.

##sets they dont allow duplicates or and arrange data randomly
set_grades = {100,100, 78,75,57} #unique and unordered 

print(f"The average is {sum(grades) / len(grades)}")
print(tuple_grades)
print(set_grades)

##method we can do on our list, tuple and set
grades.append(87) #adds items at the end of the list
print(grades)

##we can add things to a set by use of .add
set_grades.add(47)
print(set_grades)

set_one = {1,2,3,4,5,}
set_two = {1,3,5,7,11,10}

print(set_one.intersection(set_two))
print(set_one.union(set_two)) ##Remember we dont allow duplicates.

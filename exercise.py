from posixpath import split


Known_people =["Famba", "Eli", "Habib", "Sumaiya"]
person = input("Enter the Person You know:")

if person in Known_people:
    print(f"You Know {person}!")
else:
    print(f"You dont know {person}")

##Exercise
def who_do_you_know():
    #ask the user for a list of people they know.
    #split the string into a list
    #return that list.
    people = input("Please enter a List of People you know:")
    list_of_people = people.split(",") #helps us separate names from the coma points.

    people_without_spaces = [] ##create a new list that contains people without white spaces
    for person in list_of_people:
        people_without_spaces.append(person.strip()) #.strip() helps us remove tabs, whitespaces, new lines incase user typed them

    return people_without_spaces



def ask_user():
    #ask user for a name
    #see if the name is in the list of people they know
    #print out that they know the person
    person = input("Enter a name of some one you Know:")

    if person in who_do_you_know():
        print(f"You know {person}")
    else:
         print(f"you don' t know {person}")

ask_user()


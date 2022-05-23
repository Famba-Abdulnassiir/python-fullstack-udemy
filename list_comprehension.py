##list comprehension is the way to build list programatically.
my_list =[0,1,2,3,4]

an_equal_list = [x for x in range(5)]

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)

#Create a list that gives even numbers between 0 to 10
evens =[x for x in range(10) if x % 2 ==0] #it has helped us do it in a single line of code and short
print(evens)

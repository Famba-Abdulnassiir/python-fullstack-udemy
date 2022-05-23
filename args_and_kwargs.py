# In Python, we can pass a variable number of arguments to a 
# function using special symbols. There are two special symbols:

# Special Symbols Used for passing arguments:-
# 1.)*args (Non-Keyword Arguments)
# 2.)**kwargs (Keyword Arguments)


def argsKwargs(*args, **kwargs):
    ## args out put a tuple
     print(args)

     ##kwargs output a set Key word pairs.
     print(kwargs)

argsKwargs()

## How we can use them in real life
#we can rename our *args like to *num by simply adding wildcard * and any name
#  python will know its urg
def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

##Kwargs for key word pairs and here we use ** then we pass our data as Key:Value. name:Famba 
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

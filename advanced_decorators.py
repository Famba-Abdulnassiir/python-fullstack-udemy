import functools
from multiprocessing import Condition

## Formulate our Decorator with urguments.
## Please note this is important incase one wants to enter cartain type of data to data base with 
# some Condition
# it is also used in terms of if user is not admin dont show them the admin page or paid and unpaid 
# screens accordingly.

def decorator_with_urguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the Decorator!")
            if number == 56:
                print("Not running the Function")
            else:
                func(*args, **kwargs)                
            print("After the Decorator!")
        return function_that_runs_func
    return my_decorator

@decorator_with_urguments(57)
def my_function_too(x,y):
    print(x + y)

my_function_too(57, 67)

## Decorators is just a function that gets called before another fucntion eg
# @staticMethod and @classMethods

import functools

## Declare your Decorator Here
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the Decorator!")
        func()
        print("After the Decorator!")
    return function_that_runs_func

## You can Use the Decorator by invoking it as @its_name
@my_decorator
def my_function():
    print("I'm the Function")

my_function()

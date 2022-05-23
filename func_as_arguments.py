def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

## Here note we can pass add_2_nos function as parameters to methodception.
print(methodception(add_two_numbers))

## Or we can Use a Lambda Function
my_list = [13,56,77,484]


## Use Lambda Function to return a list of not thirteen.
print(list(filter(lambda x: x!=13, my_list)))

(lambda x: x*3) (5)

## Please note we can also use a function instead of lambda and get the same results
def not_thirteen(x):
    return x!=13

print(list(filter(not_thirteen,my_list)))


## Or we can use List Comprehention
print ([x for x in my_list if x != 13])
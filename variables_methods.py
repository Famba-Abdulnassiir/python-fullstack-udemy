from unittest import result


a = 5
b = 10
my_variable = 56
any_varaible_name = 10

string_variable = "hello"
single_quotes = 'String can have single quotes'

print(string_variable)
print(single_quotes)

##
def my_print_method(my_parameter):
    print(my_parameter)


my_print_method("Hello World!")

def my_multiply_method(number_one, number_two):
    return number_one * number_two

result = my_multiply_method(5,3)
my_print_method(result)

## or we can still use 
print(result)

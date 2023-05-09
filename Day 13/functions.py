# Functions are a block of reusable codes

# This is a function definition

def addition(a, b):
    return a + b


# These are function calls

addition(2, 3)
addition(4, 6)


# Return statement in a function
# if we dont return anything from a function then it returns None by default
# This is a function definition without any return and thus return None

def addition(a, b):
    print(a + b)


result = addition(3, 2)
print(result)  # None


def addition(a, b):
    return a + b


result = addition(2, 3)
print(result)  # result = 5

# Function arguments
# Python function arguments are of three types
# 1. Positional Arguments
# 2. Keyword / Default Arguments
# 3. Arbitrary arguments


# Here a, b and c are positional arguments. Positional arguments should be sent compulsorily during the function call
def summ(a , b , c):
    return a + b + c

result = summ(1, 2) # error : required positional argument
result = summ(1, 2, 3)

# Here b is a keyword / default parameter
def summm(a, b=2):
    return a + b
print(summm(2)) # it is not mandatory to send a default parameter during function call
print(summm(4, 5)) # result = 9 : default arguments are only for fallbacks
# Default values are overriden if a different value is sent during the fxn call


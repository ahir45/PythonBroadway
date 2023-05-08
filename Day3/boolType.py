# True and False are the keywords for boolean type in python
# Logical , relational , identity and membership operations returns boolean result

a = 1
b = 2
c = 0

# Logical Operations
print(bool(a) and bool(b))
print(bool(a) and bool(c))
print(bool(a) or bool(c))

# relational operations

print(a > b) # False
print(b > a) # True
print(a == b) # False
print(a != b) # True

# Identity operations

a = 1
b = 1
c = 2
print(a is b) # True
print(a is c) # False

# Membership operations

print(2 in [1, 2, 3]) #True
print(3 not in [1, 2, 3]) # False
print("h" in "hello") # True

# boolean class is subclass of int data type in python
# Thus true represents integer 1 and false represents integer 0
# Arithmetic operaation is possible for the boolean type

print(True + 1) # result = 2
print(False + 5) #result = 5
print(False * 70) # result = 0

# bool() built-in function
# bool() function can take any object as a parameter and returns true or false based on the truthy or falsy nature of the objcet.

# any non-empty strings, tuple, dictionary, set are thruthy in nature also all integers are truthy in nature except 0.

print(bool("Hello")) # True
print(bool([1, 2, 3])) # True
print(bool({"name": "john"})) # True
print(bool({1, 2, 3})) # True
print(bool(5)) # True
print(bool(-5)) # True


# All empty list, dictionary, set, string or any empty object is falsy in nature. 0 and none are falsy in nature

print(bool(None)) # False
print(bool(0)) # False
print(bool("")) # False
print(bool([])) # False
print(bool({})) # False
print(bool(False)) # False












# TUPLE DATA TYPES ARE SIMILAR TO PYTHON LIST TYPE BUT THEY ARE IMMUTABLE
# INDEXING AND SLICING IN TUPLE ARE SAME THAT OF LIST
# EMPTY TUPLE CAN BE CREATED USING PARENTHESIS  () OR tuple() BUILT-IN FUNCTION
t = tuple()
print(t)
t = ()
print(t)

t = (1, 2, 3)
print(t)

t = tuple([1, 2, 3]) # tuple() function

# CREATING A TUPLE WITH SINGLE ELEMENT
a = (1)
print(type(a)) #int

a = (1,) # WE NEED TO HAVE A COMMA WHILE CREATING TUPLE WITH SINGLE ELEMENT
print(type(a)) #tuple

# TUPLE PACKING AND UNPACKING
t = 1, 2, "Hello World" # A tuple can be created without using parenthesis as given in this example. This type of
 # tuple creating is called tuple packing

# Assigning of each tuple elements to individual variables in the LHS is called tuple unpacking
a, b, c = 1, 2, "Hello World"
print(a) # 1
print(b) # 2
print(c) # Hello World

# THIS IS HOW WE DO SWAPPING NORMALLY IN OTHER LANGUAGES WITH THE USE OF THIRD VARIABLE C
a = 1
b = 2

c = a
a = b
b = c

#SWAPPING CAN BE IMPLEMENTED EASILY IN PYTHON WITH TUPLE PACKING AND UNPACKING

a = 1
b = 2
a, b = b, a # Swapping using tuple packing/unpacking
print(a)
print(b)

# ELEMENTS IN LHS MUST BE EQUAL TO RHS IN TUPLE PAKING AND UNPACKING ELSE IT RAISES AN ERROR
a, b = 1, 2, 3 # this raises an error
a, b, c = 1, 2 # this also raises an error


# INDEXING AND SLICING IN TUPLE IS SAME AS THAT OF LIST

a = (1, 2, 3, 4, 5, 6, 7)
a[::2] # this traverse from forward jumping one step
# RESULT => (1, 3, 5, 7)

print(a[-2:-6:-1]) #providing negative step size traverse the sequence from backward
# RESULT => (6, 5, 4, 3)

print(a[::-1]) # this reverses the sequence
# REUSLT => (7, 6, 5, 4, 3, 2, 1)

# DELL KEYWORD DELETS ANY OBJECT
del a # this deletes the tuple a












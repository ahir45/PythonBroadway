# There are two types of copy for python object
# shallow copy
# Deep copy

a = [1, 2, 3]
b = a  # this increases the reference vcount of [1, 2, 3] But it's not actual copy

b.append(4)
print(a)
print(b)

# This appends the value 4 in both a and b because they both refer to the same object
b = a.copy() # this makes the shallow copy of a and assigns it to b \

# now we append a value to b, it doesn't change a
b.append(5)
print(b)
print(a)

# But the case is quite different if a list has a mutable object as an element

a = [[1, 2, 3], 4]
b = a.copy()
b[0][1] = 5
print(b) # Result - [[1, 5, 3], 4]
print(a)

# This happend because b is only a shallow copy of a

from copy import deepcopy
b = deepcopy(a)
b[0][1] = 2
print(b)
print(a) # this doesn't change value in a


# LIST COMPREHENSION


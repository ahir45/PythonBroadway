# AN EMPTY SET CAN BE CREATED USING BUILT-IN FUNCTION Set()
# SETS ARE THE MUTABLE DATATYPES IN PYTHON BUT THE ELEMENTS OF THE SET MUST BE IMMUTABLE
# SETS ARE UNORDERED DATA TYPE i.e. {1, 2} and {2, 1} ARE SAME

s = set() #Creating an empty set
print(s)

s = {2, 4, 6, 6} # A non-empty set
print(s)

s = {1, 2, 2, 3, 4, 4}
print(s) # OUTPUT: {1 ,2, 3, 4} because set elements are unique and non repeated

s = {[1, 2, 3], 4} # all elements must be immutable so this is not possible

# ADDING ELEMENTS IN SET
s = {1,2, 3}
s.add(4) #Adds 4 to set at random position
print(s)

s.update([5, 6, 7]) # We can use update() method to update a set. it takes iterable/sequence as a parameter
print(s) # OUTPUT : {1, 2, 3, 4, 5, 6, 7}

# REMOVING ELEMENTS IN A SET

s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s.remove(8) #remove() method takes value (not index) as a parameter
print(s)

# THE DIFFERENCE IN DISCARD AND REMOVE METHOD IS REMOVE RAISES AN ERROR IF THE VALUE TO BE REMOVED IS NOT PRESENT IN SET.
# BUT DISCARD METHOD RETURN NONE IF THE VALUE TO BE REMOVED IS NOT PRESENT IN THE SET

s.discard(5) #OUTPUT: {1, 2, 3, 4, 6, 7, 8, 9, 10}
print(s)

s.pop() # It pops out an element from a random position in set
print(s)

s.clear() # It clears the set
print(s)



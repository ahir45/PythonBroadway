s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7 ,8}

s = s1.union(s2) #It gives union of two sets
print(s)
s = s1.intersection(s2)
print(s)
s1.isdisjoint(s2) # s1 and s2 are not a disjoint set as they have common elements 4 and 5. So it gives false
s1.symmetric_difference(s2) # this is a complement of s1 intersection of s2
print(s) # result = {1, 2, 3 ,6, 7, 8}

s1.symmetric_difference_update(s2)
# this updates the symmetric difference of s1 and s2 to s1

s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 4}
print(s2.issubset(s1)) #true
print(s1.issuperset(s2)) #true
print(s1.issuperset(s1)) #false

# BITWISE OPERATORS IN SET OPERATION

s = s1 | s2 #UNION => same as s1.union(s2)
s = s1 & s2 #INTERSECTION => same as s1.intersection)s2)
s = s1 - s2 #DIFFERENCE => same as s1.difference(s2)
s = s1 ^ s2 #SYMMETRIC DIFFERENCE => same as s1.symmetric_difference_update(s2)


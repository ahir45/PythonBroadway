# a = 1
# b = 2
# print(a+b)
# print(a-b)
# print(b%a)

#Logical Operations
# And
print(True and False)
print(False and False)
print(True and True)
print(False and True)

#Identity Operator

# is and isnot are the identity operator

a = 1
b = 1
print(a is b)
b = 123
print(a is b)
print( a is not b)


# Membership Operator
ages =[21, 22, 23, 27]
print(22 in ages)
print(22 not in ages)

name = "Broadway"
print(a in name)

# "=" is the simplest assignment operator
a += 1 #this is assignment operator

#Precedance and associativity
# Precende is the rule which determines the priority of operators in an operation
#Associativity is the rule that determines the priority of operators if one or more operators have the same precedence
#Normally Associativity is from left to right but for ** operator it is from right-left

print(3**2**3)
#First 2**3 is evaluated then the result is raised to the power of 3


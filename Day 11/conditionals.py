# condition statements allow us to make decisions in a program
# we use if else block for the condition check

# We can write relational operations, logical, identity, membership operations, truthy and falsy values with if statement

a = 1
b = 2

if bool(a) and bool(b):
    print("Hello")

if bool(a) and bool(0):
    print("Hello")

if bool(a) or bool(b):
    print("Hello")

# Identity operation

a = 1
b = 1
if a is b:
    print(a)
b = 2
if a is b:
    print(b)

# Membership Operation

a = [1, 2, 3, 4]
if 2 in a:
    print(a)

if 5 not in a:
    print(a)

# Truthy and Falsy with if

a = [1, 2, 3, 4]
if a:   # truthy condition
    print(a)
a = []
if a:    # falsy condition
    print(a)

m = 0
if a:
    print(m)

# if ... else block

a = ""
if a:
    print(a)
else:
    print("It is empty")

# Ternary if .. else block

a = "hello world "
print(a) if a else print("it is empty")

a = 5
b = 4
print(a) if a > b else print(b)

# if .. elif.. elif..else ladder

a = 5
b = 4

if a > b:
    print(a)
elif b == a:
    print(b)
elif b > a:
    print(a)
else:
    print(b)
    



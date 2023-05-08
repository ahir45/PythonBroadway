a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

if a > b and a > c:
    print("Greatest is", a)
elif b > a and b > c:
    print("Greatest is ", b)
else:
    print("Greatest is ", c)



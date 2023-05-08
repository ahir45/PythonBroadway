# a = range(1, 30)
# if a <= 30:
#     if a % 3 == 0:
#         print("Fizz")
#     elif a % 5 == 0:
#         print("Buzz")
#     elif (a % 5 == 0) and (a % 3 == 0):
#         print("FizzBuzz")
#     else:
#         print(a)

# loop over a range of numbers from 1 to 100 (inclusive)
for num in range(1, 101):
    # if the number is divisible by bo th 3 and 5, print "FizzBuzz"
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # if the number is divisible by 3, print "Fizz"
    elif num % 3 == 0:
        print("Fizz")
    # if the number is divisible by 5, print "Buzz"
    elif num % 5 == 0:
        print("Buzz")
    # otherwise, print the number
    else:
        print(num)

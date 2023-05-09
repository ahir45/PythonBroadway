# treating n as string

a = int(input("Enter the number: "))
a_str = str(a)
if a_str == a_str[::-1]:
    print("Its palindrome")
else:
    print("Its not a palindrome")


# Treating n as integer

n = int(input("Enter a number : "))
reverse = 0
b = n
while n != 0:
    remainder = n % 10
    reverse = reverse * 10 + remainder
    n = n // 10
if reverse == b:
    print("Palindrome")
else:
    print("Not palindrome")


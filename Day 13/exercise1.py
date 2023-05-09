S = "All the occurrences of a specified character in a given string"
inputt = input("Enter the character : ")
new_S = ""
for s in S:
    if s != inputt:
        new_S += s

print(new_S)

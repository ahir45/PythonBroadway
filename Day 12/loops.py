# vowels = ["a", "e", "i", "o", "u"]
# for vowel in vowels:
#     if vowel == "i":
#         break
#     print(vowel)
#     print(1)

count = 0
while count < 10:
    if count == 5:
        continue
    print(count)
    count += 1


# pass ####

# to avoid syntax error if we want to create a function to use it in future
# pass is used when we know that we need a function or class in future but the logic is unclear currently.

def addition():
    pass  # logic is added here in future

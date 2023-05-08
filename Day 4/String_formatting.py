# STRING FORMATTING USING PERCENTAGE

m = "Hello I'm %s. I'm %d years old" %("Abhi", 27)
print(m)

m = "I have Rs. %.2f" % (30.333)
print(m)

# STRING FORMATTING USING FORMAT METHOD

m = "Hello I'm {}".format("john")
print(m)

m = "I'm {age} years old".format(age=22)
print(m)

m = "I have {0}, {1} and {2}".format("pen", "pencil", "copy")
print(m)
m = "I have {1}, {0} and {2}".format("pen", "pencil", "copy")
print(m)

# IF YOU DON'T GIVE INDEX AND HAVE MULTIPLE PLACEHOLDERS THEN THE VALUES ARE TAKEN IN ORDER

m = "I have {}, {} and {}".format("pen", "pencil", "copy")
print(m)

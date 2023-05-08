m = "hello world"
print(m.capitalize())
print(m.title())
print(m.upper())
print(m.lower())

results = m.split()
print(results)
results = m.split('e') #Splits from 'e'
result = m.split('o')
print(result)

a ="+"
print(a.join(m))

message = ["Hello" , "World"]
"".join(message)
"+".join(message)

m = "Hello World"
result = m.find("Wo")
print(result)
result = m.find("Wooo")
print(result) #output = -1

result = m.replace('World', 'world')
print(result)

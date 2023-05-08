student = {"name": "John", "age": 25}

print(all(student)) # returns true if all the values are truthy. This is like and operation
print(all([])) # this is an exception because it gives true

a = []
value = True
def all(a):
    for i in a:
        if bool(i) is False:
            return False
        return value

all([])

print(any(student)) # This gives true. any() returns true if any of the elements in an iterable is truthy. This is like or operation
print(any([])) # this gives false

result = sorted(student)
print(result)


# Dictionary methods contd
# mostly used in loops
student = {"name": "John", "age": 25}
print(student.items()) # it gives list like object => dict_items([('name', 'John'), ('age', 25)])
print(student.keys()) # it gives list like object of dictionary keys => dict_keys(['name', 'age'])
print(student.values()) # it gives list like object of dictionary vlaues =>  dict_values(['John', 25])

d = student.fromkeys([1, 2, 3], "Hello")
print(d) # gives a new dictionary with keys of iterable with common value result => {1: 'Hello', 2: 'Hello', 3: 'Hello'}

d = student.fromkeys([1, 2, 3])
print(d)  #result=> {1: None, 2: None, 3: None}


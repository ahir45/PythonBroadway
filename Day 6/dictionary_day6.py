# CREATING AND EMPTY DICTIONARY
d = dict()
d = {}

# DICTIONARY TYPES is the key value pair data type
# Empty dictionary can be created using curly braces {} or dict() built-in function

student = {"name": "John", "age": 45, "department": "CS"}
print(student)
student = dict(name="JOhn", age=45, department="CS") # non empty dictionary ||| Here name, age and department is an idenifier
print(student)

student = [
    {"name": "S1", "age": 45},
    {"name": "S2", "age": 15}
]
# student = dict([
#     ("name", "John")
#     ("age", 45)
#     ("department", "CS")
# ])

# ACCESSING VALUES IN DICTIONARY

student = {"name": "John", "age": 45, "department": "CS"}
name = student['name']
print(name) # result = John

print(student['department'])

# We can also access the dictionary values using get() method
name = student.get('name')
print(name)

roll = student.get('roll')
print(roll) # this gives none. If the key is not present in the dictionary is provided to the get() method then returns it none

# WE CAN ALSO PROVIDE A DEFAULT VALUE TO THE get() METHOD

roll = student.get("roll_number", 4) # here 4 is a default value
print(roll) #this gives 4

name = student.get("name", "Jane")
print(name) #result = John

# ADDING AND UPDATING DICTIONARY

d = {"name": "John", "age": 45, "department": "cs"}
d["roll"] = 4
print(d)
 # if the key is present then it gets updated
d["name"]="Jane"
print(d)

# UPDATING DCTIONARY USING UPDATE() METHOD

student = {"name": "John", "age":45}
student.update({"department": "CS", "roll": 4})
print(student)
student.update(id=1, height=5.8)
print(student)

# DELETING/REMOVING DICTIONARY KEY-VALUES
student = {'name': 'John', 'age': 45, 'department': 'CS', 'roll': 4, 'id': 1, 'height': 5.8}
roll = student.pop("roll")
print(student) # roll key is removed from the dictionary
print(roll)

#When given multiple keys last key overrides the previous one like if we give multiple key name the value of last key name is returned

# RULES FOR DICTIONARY KEYS
# 1. DICTIONARY KEYS MUST BE IMMUTABLE
# 2. DICTIONARY VALUES CAN BE OF ANY DATA-TYPE
# 3. A TUPLE CAN ALSO BE A DICTIONARY KEY BECAUSE IT IS IMMUTABLE TYPE. BUT IF CONTAINS A MUTABLE TYPE, THEN IT CAN'T BE USED AS A KEY

# EG d = {(1, 2, [1,2]) : "Hello"

#MEMBERSHIP OPERATION IN DICTIONARY

student = {"name": "John", "age": 23}
print("age" in student) # True. Membership is checked in keys in a dictionary
print("department" in student) # False


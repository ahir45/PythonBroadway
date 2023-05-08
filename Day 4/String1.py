# strings in python are of immutable type
# We can create empty string using str() built-in function or using empty single or double quotes

example = "" # empty string
example = str() #Empty string

 # Escape sequences
 # Escape sequences are the strings in python which supresses ususal meaning of the cahracter and gives a new meaning

example = 'I\'m learning Python' # Here \' is an escape sequence
print(example)

example = "Path to my folder is C:\\Project\\Broadway" # Here \\ is an escape sequence
print(example)

example = "Hello\nWorld" # new line escape charcter
print(example)

example = "Hello\tWorld" # escape character for tab
print(example)

example = "Hello \bWorld" # here \b is escape character for a backspace
print(example)


# Tripple Quoted String

example = ''' 
Example 1 
'''
print(example) # Example with tripple single quotes

example ="""
Example 2
"""
print(example) # Example with tripple double quotes

example = """
I'm learning Python
"""
print(example) # we don't need to use escape sequence characters

# INDEXING AND SLICING IN STRING
# String indexing and slicing is similar to the list slicing and indexing

message = "Hello World"
print(message[3]) # output = l
print(message[6]) # output = W
print(message[-2]) # negative indexing is also possible output = l
print(message[1:7]) #result => 'ello W'
print(message[1:-3]) # output = 'ello Wo'
print(message[-7:-3]) # output = '0 Wo'
print(message[-3:-7]) #output= ''
print(message[1:7:2]) #output = ''

# String doesn't support item assignment because it is immutable

message = "Hello"
message[1] = "E" #This is not possible



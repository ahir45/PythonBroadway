l = [(2,3), (1,1), (4,2), (5,5), (2,4)]

# Arrange the list on the basis of second element of each item in the list

def get_second_number(data):
    return data[1]
l.sort(key=get_second_number)
print(l)

a = [(4,12,5), (6,1), (11,12), (6,7,8)]

# sort the list based on the last item of each tuple inside the list

def get_number(data):
    return data[-1]
a.sort(key=get_number)
print(a)

# list.reverse()

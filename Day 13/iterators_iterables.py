# iterators are those objects which can be iterated/looped through
# iterables are those objects which can be converted to iterators

# tuple, dict, lists, set are the examples of iterables

a = [1, 2, 3, 4]
iter_a = a.__iter__()
iter_a = iter(a)

print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
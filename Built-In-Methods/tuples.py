# A tuple is a collection which is ordered and unchangeable.
#  - Allows duplicates
my_tuple = (1, 2, 3, 'hey', 5, 'hey')
print(my_tuple)

# count() - Return the number of times value occurs in the tuple
# tuple.count(value)
print(my_tuple.count('hey'))

# index() - Return the index of the first occurrence of value
#  - If not found, raises a ValueError
# tuple.index(value[, start[, end]])
print(my_tuple.index('hey', 4))
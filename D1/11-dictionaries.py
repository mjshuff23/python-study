my_dict = {'a': 1, 'b': 2}

# If this key doesn't exist, line 5 will error out
x = my_dict['a'] 
# print(x)

# Returns None because the key 'afdsf' does not exist in the dictionary.
x = my_dict.get('af')
# print(x)

# Get a list(dict_keys) of all the keys in the dictionary
x = my_dict.keys()
# print(x)

# The list of the keys is a view of the dictionary. If you change the 
# keys by adding or removing, the list will change
my_dict['c'] = 'new value'
# print(x)

# Get the values of the dictionary
x = my_dict.values()
# print(x)

# The list of the values is a view of the dictionary. If you change the 
# values, the list will change
my_dict['a'] = 'WHAT UP'
# print(x)

# items() returns a list of tuples from a dictionary
x = my_dict.items()
# print(x)

# The items() list returned is a view of the items of a dictionary, meaning
# that any changes done to the dictionary will be reflected in x
my_dict['I LOVE CHEESE'] = 'CHEESE'
# print(x)

# Check if a key exists
# print(my_dict)
# print('a' in my_dict)
# if ('b' in my_dict):
    # print('b exists')

# update() method
d = {1: 'one', 2: 'two'}
d1 = {2: 'three', 4: 'four'}
# print(d)
# print(d1)
d.update(d1)
# print(d)
# print(d1)

# removing a key/value pair, use dict.pop(key), returns the value
x = d.pop(4)
# print(d)
# print(x)

# The popitem() method removes the last inserted item (in versions before 3.7,
#  a random item is removed instead) as a tuple (key, value) from the dictionary
x = d.popitem()
# print(x)

# The del keyword removes the item with the specified key from the dictionary.
new_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# del new_dict['a']
# print(new_dict)

# The del keyword can also delete the entire dictionary
# del new_dict
# print(new_dict)

# The clear() method empties the dictionary
new_dict.clear()
print(new_dict)
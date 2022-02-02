my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# clear() - Remove all items from the dictionary
# dict.clear()
my_dict.clear()
print(my_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# copy() - Return a shallow copy of the dictionary
#  - This means we can change literals without affecting the original
#  - However, deeper levels will be references
# dict.copy()
my_dict_copy = my_dict.copy()
print(my_dict_copy)

# fromkeys() - Return a new dictionary with keys from parameter 1 and values set to value of parameter 2
# dict.fromkeys(seq[, value])
my_dict_fromkeys = dict.fromkeys(['a', 'b', 'c', 'd'], 1)
print(my_dict_fromkeys)

# get() - Return the value of the specified key
#  - If not found, returns "None" when no default value is specified
# dict.get(key[, default])
my_dict_get = my_dict.get('abc', 'default')
print(my_dict_get)

# items() - Return a new view of the dictionary's items
# dict.items()
my_dict_items = my_dict.items()
print(my_dict_items)

# keys() - Return a new view of the dictionary's keys
# dict.keys()
my_dict_keys = my_dict.keys()
print(my_dict_keys)

# pop() - Remove the item with the specified key
# dictionary.pop(keyname, defaultvalue)
#  - If defaultvalue is not specified, and no item with the specified key is found, an error is raised
my_dict_pop = my_dict.pop('a')
print(my_dict_pop)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# popitem() - Removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.
# dict.popitem()
my_dict_popitem = my_dict.popitem()
print(my_dict_popitem)

# setdefault() - Return the value of the specified key. If the key does not exist, insert the key, with the specified value, into the dictionary
# dict.setdefault(key, default=None)
my_dict_setdefault = my_dict.setdefault('abdfa')
print(my_dict_setdefault)

# update() - Update the dictionary with the key/value pairs from another iterable
# dict.update(iterable)
print(my_dict)
my_dict.update({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(my_dict)
my_dict.update([('e', 5), ('f', 6), ('g', 7), ('h', 8)])
print(my_dict)

# values() - Return a new view of the dictionary's values
# dict.values()
my_dict_values = my_dict.values()
print(my_dict_values)
my_dict['a'] = 'WHAT UP'
print(my_dict_values)
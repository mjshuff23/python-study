#### BUILT-IN FUNCTIONS ########################################################
#
### Functions Using Iterables #######
# - Python has a number of built-in functions to make it easy for developers to 
#    work with iterables such as sequences and collections.
#
## filter()
# - filter(function, iterable) creates a new iterable of the same type which 
#    includes each item for which function returns True.
#   - Parameters
#       - function: takes an item (from the iterable) and returns a Boolean
#       - iterable: e.g. list, tuple, range, dictionary, set, or str
#
## map()
# - map(function, iterable) creates a new iterable of the same type which 
#    includes the result of calling the function on every item in the iterable.
#   - Parameters
#       - function: takes an item (from the iterable) and returns another item
#          (of same or different type)
#       - iterable: e.g. list, tuple, range, dictionary, set, or str
#
## sorted()
# - sorted(iterable, key=None, reverse=False) creates a new sorted list from 
#    the items in iterable
# - Notice that the output is always a list.
# - Parameters
#   - iterable: e.g. list, tuple, range, dictionary, or set
#   - key: optional function which converts an item to a value to be compared 
#     (e.g. key=str.lower for case-insensitive sorting on a list of strings)
#   - reverse: optional boolean
# - The parameters key and reverse must be set using the name and an equal sign
#
## enumerate()
# - enumerate(iterable, start=0) starts with a sequence and converts it to a 
#    series of tuples. Each tuple is made up of two elements: index and value.
# - The parameter start must be set using its name and an equal sign.
# - The best way to understand enumerate is to consider an example.
quarters = ['First', 'Second', 'Third', 'Fourth']
print(enumerate(quarters))
print(enumerate(quarters, start=1))
(0, 'First'), (1, 'Second'), (2, 'Third'), (3, 'Fourth')
(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')

## zip()
# - zip(*iterables) creates a zip object filled with tuples that combine 1-to-1 the items in each provided iterable. If the iterables have uneven length then zip stops when the shortest one runs out of items.
#  - Parameters
#   - two or more iterables: usually lists, tuples or dictionaries
#
### Functions That Analyze Iterables
# - Another set of built-in functions can be used to discover more about the 
#    data within an iterable.
#
## len()
# - len(iterable) returns the count of the number of items. Works on 
#    collections (dictionary and set) as well as sequences (list, tuple, range 
#    or string).
#
## max()
# - max(*args, key=None) returns the largest of two or more arguments
# - max(iterable, key=None) returns the largest item in the iterable
# - Parameters
#   - args: a series of items separated by commas
#   - iterable: e.g. list, tuple, dictionary or set
#   - key: optional function which converts an item to a value to be compared (e.g. key=str.lower for case-insensitive string comparison)
# - The parameter key must be set using its name and an equal sign.
#
## min()
# - (Same as max returning the item with the smallest value.)
#
## sum()
# - sum(iterable) is usually used with a list of numbers to generate the total.
#
# - IMPORTANT: There is a faster way to concatenate an array of strings into 
#              one string so sum should not be used for that.
#
# - Optional challenge: Think about how you could calculate the average of a 
#                       list of numbers in one line of Python code.
#
## any()
# - any(iterable) returns True if any items in the iterable are true.
#
# - If the iterable is empty, then any returns False because it cannot find any 
#  true items.
#
# - This depends on the expanded definition of truth in Python where numbers 
#    are true when not zero, strings are true when not empty, and other kinds 
#    of objects are true when not None.
#
## all()
# - This is a companion function to any above and also depends on the expanded 
#   definition of truth.
#
# - all(iterable) returns True if all items in the iterable are true.
#
# - If the iterable is empty, then all returns True because it did not find any 
#    items that were false.
#
### Working With Dictionaries
#
## dir()
# - dir(dictionary) returns the list of keys in the dictionary.
#
# - It can also be used on objects or modules to return a list of their
#    attributes.
#
### Working With Sets
#
## union()
# - The `|` operator or union(*sets) function can be used to produce a new set 
#    which is a combination of all elements in the provided sets.
a = {1, 2, 3}
b = {2, 4, 6}
print(a | b)
# - Remember, sets do not allow duplicates. That is why 2 only appears once in 
#    the result in this example.

## intersection()
# - The `&` operator or intersection(*sets) function can be used to produce a 
#    new set of only the elements that appear in all sets.
a = {1, 2, 3}
b = {2, 4, 6}
print(a & b)

## difference() and symmetric_difference()
# - The `-` operator or difference(*sets) function can be used to produce a new 
#    set of only the elements that appear in the first set and NOT the other(s).
#
# - The `^` operator or symmetric_difference(*sets) function can be used to 
#    produce a new set of only the elements that appear in EXACTLY ONE set and 
#    NOT in both (or all) sets.
a = {1, 2, 3}
b = {2, 4, 6}
print(a - b)
print(b - a)
print(a ^ b)

#
#
#
################################################################################
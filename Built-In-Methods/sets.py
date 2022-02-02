# A set is a collection which is unordered, unchangeable*, and unindexed.
my_set = {'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'}
print(my_set)

# add() - Add an element to the set
# set.add(element)
my_set.add('e')
print(my_set)

# clear() - Remove all elements from the set
# set.clear()
my_set.clear()
print(my_set)

my_set = {'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'}

# copy() - Return a shallow copy of the set
# set.copy()
my_set_copy = my_set.copy()
print(my_set_copy)

# difference() - Return the difference of two or more sets as a new set
# set.difference(iterable)
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

my_set_difference = x.difference(y)
my_other_set_difference = y.difference(x)
print(my_set_difference)
print(my_other_set_difference)

# difference_update() - Remove all elements of another set from this set
# set.difference_update(other_set)
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.difference_update(y) # Remove all elements of y from x (apple)
print(x)
print(y)

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
y.difference_update(x) # Remove all elements of x from y (apple)
print(y)

# discard() - Remove the specified element from a set if it is a member. If the element is not a member, do nothing
#  - This is different from remove() which will raise an error if the element 
#     is not in the set
# set.discard(element)
my_set_discard = {'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'}
my_set_discard.discard('a')
print(my_set_discard)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# append() - Append an element at the end of the list
# list.append(ele)
my_list.append(11)
print(my_list)

# clear() - Remove all elements from the list
# list.clear()
my_list.clear()
print(my_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# copy() - Return a shallow copy of the list
#  - This means we can change literals without affecting the original
#  - However, deeper levels will be references
# list.copy()
my_list_copy = my_list.copy()
print(my_list_copy)

# count() - Return the number of elements with a specific value
# list.count(ele)
print(my_list.count(1))

# extend() - Add all elements of a list (or any iterable) to the end of the current list
# list.extend(iterable)
my_list.extend([11, 12, 13])
print(my_list)

# index() - Return the index of the first element with the specified value
# list.index(ele)
print(my_list.index(6))

# insert() - Insert an element at a given position
# list.insert(index, ele)
my_list.insert(2, "inserted")
print(my_list)

# pop() - Remove and return an element at a given position
# list.pop(index)
my_value = my_list.pop(2)
print(my_value)

# remove() - Remove the first item with the specified value
# list.remove(ele)
my_list.remove(1)
print(my_list)

# reverse() - Reverse the order of the list
# list.reverse()
my_list.reverse()
print(my_list)

# sort() - Sort the list
# list.sort()
my_list.sort()
print(my_list)


# abs() - Absolute value
print(abs(-5))

# all() - Returns `True` if all elements of the iterable are true
#  (or if the iterable is empty).
my_list = [True, False, True]
print(all(my_list))

# any() - Returns `True` if any element of the iterable is true.
print(any(my_list))

# bin() - Print binary value of number
print(bin(12314))

# bool() - Returns `True` if the value is true, `False` otherwise.
print(bool(0))
print(bool(1))

# dict() - Create a dictionary
x = dict(name = "John", age = 36, country = "Norway")

# dir() - Return a list of properties/methods of an object
print(dir(x))

# filter() - Returns an iterator yielding those items of iterable for 
#  which function(item) is true
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# callback function
def is_an_int(num):
    return isinstance(num, int)
answer = filter(is_an_int, nums)
print(list(answer))

# lambda functions - one liners
# lambda arguments : expression
my_lambda = lambda x: type(x) == int
answer = filter(my_lambda, nums)
print(list(answer))

# format() - Format a string
# format(value, format)
print("Hello, {0}".format("world"))
print(format(0.5, '%'))

# enumerate() - Return an enumerate object. It produces a sequence of tuples
#  containing an index and a value.
x = ("apple", "banana", "cherry")
y = enumerate(x)
## Must convert to a list
print(y)
print(list(y))

# frozenset() - Return a frozenset object. A frozenset is an immutable set.
# It is implemented as a class and behaves like a set.
z = frozenset(x)
print(z)

# delattr() - Delete an attribute from an object (property/method)
class Person(dict):
    name = "John"
    age = 23
    country = "Norway"

delattr(Person, 'age')
# print(Person.age) # AttributeError: 'Person' object has no attribute 'age'

# getattr() - Get an attribute from an object 
# getattr(object, attribute, default)
print(getattr(Person, 'age', 24))

# setattr() - Set an attribute on an object
# setattr(object, attribute, value) - If the attribute doesn't exist, creates it
setattr(Person, 'sadfasage', 44)
print(Person.sadfasage)

# hasattr() - Check if an object has an attribute
# hasattr(object, attribute)
print(hasattr(Person, 'age'))

# hex() - Return the hexadecimal representation of an integer
# hex(x)
print(hex(123))

# input() - Read a string from standard input
# input(prompt)
# my_name = input("What is your name? ")
# print(my_name)

# isinstance() - Return `True` if the object is of the specified type
# isinstance(object, classinfo)
print(isinstance(12, int))

# issubclass() - Return `True` if the object is an instance of the specified
# issubclass(class, classinfo)
print(issubclass(int, object))

# iter() - Return an iterator from an object
# iter(obj[, sentinel])
x = list(iter(range(10)))
print(x)

# len() - Return the length of an object
# len(data)
print(len("Hello"))

# list() - Return a list from the iterable
# list(iterable)
print(list(range(10)))

# map() - Apply a function to every item of a list and return a list of results
ab = list(map(lambda x: x * 2, x))
print(ab)

# max() - Return the largest item in an iterable or the largest of two or more
#  arguments
# max(iterable)
print(max(x))
print(max(ab))
print(max(1, 10, 1000000))

# min() - Return the smallest item in an iterable
# min(iterable)
print(min(x))

# next() - Return the next item of an iterator
# next(iterator[, default])
x = iter(range(10))
print(next(x))
print(next(x))

# open() - Open a file, returns a file object
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None,
#  closefd=True, opener=None)
#   - file - Name of the file.
#   - mode - Mode to open the file. (r, w, a)
# read_stream = open("test.txt", "r")
# print(read_stream.read())


# reversed() - Return a reversed iterator
# reversed(seq)
print(list(reversed(list(range(10)))))

# round() - Round a number to a given precision
# round(number, ndigits=0)
print(round(1.23456, 2))
print(round(1.23456, 1))
print(round(number=1641.23456, ndigits=-3))

# set() - Create a set
# set(iterable)
my_set = set(range(10))
print(my_set)

# slice() - Creates a tuple slice object
# slice(start, stop[, step])
my_list = [1, 5, 3, 0, 5, 6, 75, 8, 9, 10]
x = slice(0, 10, 2)
print(my_list[x])

# sorted() - Return a sorted list from the iterable
# sorted(iterable, key=None, reverse=False)
print(sorted(my_list))
print(sorted("This is a test string from Andrew".split(), key=str.lower))

# sum() - Return the sum of an iterable
# sum(iterable)
print(sum(range(10)))

# tuple() - Create a tuple
# tuple(iterable)
print(tuple(range(10)))

# type() - Return the type of an object
# type(object)
print(type(x))

# zip() - Return a zip object which produces tuples
# zip(iter1 [, iter2 [...]]) - iter1 will be index 0, iter2 will be index 1, etc
x = list(zip(range(10), range(10, 20)))
print(x)
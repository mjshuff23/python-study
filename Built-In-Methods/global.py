# abs() - Absolute value
print(abs(-5))

# all() - Returns `True` if all elements of the iterable are true
#  (or if the iterable is empty).
my_list = [True, False, True]
print(all(my_list))

#  any() - Returns `True` if any element of the iterable is true.
print(any(my_list))

# bin() - Print binary value of number
print(bin(12314))

# bool() - Returns `True` if the value is true, `False` otherwise.
print(bool(0))
print(bool(1))

# delattr() - Delete an attribute from an object (property/method)
class Person(dict):
    name = "John"
    age = 23
    country = "Norway"

delattr(Person, 'age')
# print(Person.age) # AttributeError: 'Person' object has no attribute 'age'

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

# getattr() - Get an attribute from an object 
# getattr(object, attribute, default)
print(getattr(Person, 'age', 24))

# setattr() - Set an attribute on an object
# setattr(object, attribute, value)
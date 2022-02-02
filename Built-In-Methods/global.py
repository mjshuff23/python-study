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

# lambda functions - lambda arguments : expression
answer = filter(lambda x: type(x) == int, nums)

print(list(answer))
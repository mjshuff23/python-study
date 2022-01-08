# Duck typing is a programming style which avoids checking an object's "type" 
#  to figure out what it can do. In other words, duck-typing avoids tests for type() or isinstance().
# Instead a method or attribute is simply called or used in the code. If necessary a check would be for hasattr(). This approach is also known as EAFP: Easier to ask for forgiveness than permission
# By focusing on interfaces, duck-typing makes well-designed code more flexible.
# Python uses duck-typing as its fundamental approach.

#### Assigning Variables
# Python has no variable declaration keyword such as let, var or const. 
#  Instead, the assignment of a value automatically declares a variable.
a = 7
b = 'Marbles'
print(a)
print(b)

# Variable assignment can be chained to give several variables the same 
#  initial value.
count = max = min = 0
print(count)
print(min)
print(max)

# The value - and even the type - of a variable can be reassigned at any time.
a = 17
print(a)
a = "John"
print(a)

# Unlike JavaScript, Python will not return NaN as the result of calculations; 
#  instead, it throws exceptions.
a = '7'
# a /= 2 # TypeError: unsupported operand type(s) for /=: 'str' and 'int'
print(a)

# If you absolutely have to have it, you can create "not a number" by sending the string "nan" into the float constructor.
print(float("nan"))

#### None
# Python's replacement for null is None. It is used to indicate a variable has 
#  no value.
# 
# None is very special because it is actually an object (of type NoneType). 
#  That means it can be used wherever other objects are used.
my_var = None
print(my_var is None)     # => True
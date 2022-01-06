########## BOOLEAN DATA TYPE
# - Can be True or False (notice the capital letter)

### Logical Operators
# - Python's version of logical operators are plain English:
#     - and
print(True and True) # => True
print(True and False) # => False
print(False and False) # => False
#     - or
print(True or False) # => True
print(True or True) # => True
print(False or False) # => False
#     - not
print(not True) # => False
print(not False and True) # => True
print(not True or False) # => False

# The rules of logic apply in Python as in every other language, including DeMorgan's Law.
#   - not (A or B) is equivalent to not A and not B
#   - not (A and B) is equivalent to not A or not B

# Truth Value Testing
# Python considers an object to be true (notice the lower case 't') UNLESS it is one of the following:
#   - constant: None or False
#   - zero of any numeric type: 0, 0.0
#   - empty sequence or collection
#   - string: ''
#   - list: []
#   - tuple: ()
#   - dictionary: {}
#   - set()
#   - range(0)
# In other words, all items in this list are False and everything else is true.
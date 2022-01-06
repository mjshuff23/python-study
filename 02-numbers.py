# Single Line Comments

# Multi-Line Comments / Documentation / Help
"""Summary Line

Description
"""

print('hi\n') # Printing
num = 30000 # Declaration and Initialization of a variable

def my_function(): # Notice in Python, we use underscores instead of camelCase
    """My Function Documentation
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    print('test')

# How to see multi-line documentation
help(my_function)

my_function()

###### NUMBERS ################################################################
# Python has three numeric types

# Integer - Counting numbers, both positive and negative, with no decimal point
#         - Can use the int() constructor for creation/conversion
#         - Interesting fact: Boolean is a subtype of integer in Python.
print(3)
print(int(1.9)) # Truncates everything after the decimal
print(int())

# Floating Point - Decimal numbers.  Internal precision (number of decimal 
#                   places) and representation (how they're stored) can change
#                   slightly depending on the machine on which your program runs
#                - Floating point numbers are created using numbers with a 
#                   decimal point, with the float() constructor, or using
#                   scientific notation.
print(2.24)
print(2.)
print(float())
print(float(4))

# Complex Numbers - Consist of a real part and an imaginary part.  In
#                    mathematics they are written as `5 + 7i` where 5 is
#                    the real part and the 7 is the imaginary part.  In
#                    programming the `i` is often switched to a `j`.  Python
#                    follows this practice
#                 - The imaginary part of a complex number can be specified by
#                    appending j or J to a number (which makes an imaginary 
#                    part with zero real part). Complex numbers are created by 
#                    adding a real part to an imaginary part or using the 
#                    complex() constructor. If omitted, the imaginary part 
#                    defaults to zero.
#                 - Fun fact: Both the real part and the imaginary part of a
#                    complex number are stored as floating point numbers
print(7j)  # => 7j
print(5.1 + 7.7j) # => 5.5+7.7j
print(complex(3, 5)) # => 3 + 5j - First parameter is real and the second is
#                                  imaginary
print(complex(17)) # => 17+0j
print(complex()) # => 0j

# Type Casting - When one type of number is converted to another
print(17)
print(float(17)) # int-to-float
print(17.0)
print(int(17.0)) # float-to-int
print(str(17.0) + ' and ' + str(17)) # float-to-string and int-to-string

# Arithmetic Operators
print(5+5) # 10 - Addition
print(5-5) # 0 - Substraction
print(5*5) # 25 - Multiplication
print(5/5) # 1 - Division
print(5%5) # 0 - Modulo (Remainder)
print(5**2) # 25 - Exponent
print(5//2) # 2 - Integer Division

## Assignment Shorthand - Note that ++ and -- don't exist in Python
my_num = 5
my_num += 5 # my_num = my_num + 5
my_num -= 5 # my_num = my_num - 5
my_num *= 5 # my_num = my_num * 5
my_num /= 5 # my_num = my_num / 5
my_num %= 5 # my_num = my_num % 5
my_num **= 5 # my_num = my_num ** 5
my_num //= 5 # my_num = my_num // 5
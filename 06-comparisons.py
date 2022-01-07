##### COMPARISON OPERATORS ############################
print(5 > 2) # => True
print(2 < 5) # => True
print(2 == 2) # => True
print(2 != 2) # => False
print(2 <= 2) # => True
print(2 >= 2) # => True

# Logical operators (and, or, not) and equality operators (<, <=, >, >=, ==, 
#  !=) are often combined to form complex and useful logic. It is important to 
#  understand how a combination will be understood by the Python language.
# In Python, the equality operators are processed from left to right before the logical operators.
# Then the logical operators are processed in this order:
#    - not
#    - and
#    - or

### Strict Comparisons ########
# Python has a different way to handle strict comparisons: is and is not.
#
# Numbers, come in several types; for example, with or without a decimal point. 
#  The equality operator (==) considers them equal, but the identity operator
#  (is) does not.
print (2 == 2.0)    # => True
print (2 is 2.0)    # => False
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
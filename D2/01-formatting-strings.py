#### FORMATTING STRINGS ########################################################
import datetime

### Join #######################################################################
# - A common request is to take a list and `join` them together into a single 
#   string. Often a separator is needed to make the data look pretty. Often 
#   this is a space, comma, line break; or perhaps a dash in the case of zip 
#   codes and phone numbers.
#
# - In Javascript the join function was available on arrays. In Python, 
#    however, this is flipped around. The join function is actually on strings.
shopping_list = ['bread','milk','eggs']
print(', '.join(shopping_list)) # bread, milk, eggs

### Formatting Printing ########################################################
# - Python has a very powerful formatting engine for making exactly the strings 
#   you need. The format function is one way to apply these options. Like join, 
#   format is applied to strings.

## Comma as thousands separator
print('{:,}'.format(1234567890))

## Date and Time
d = datetime.datetime(2020, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

## Percentage
points = 190
total = 220
print('Correct answers: {:.2%}'.format(points/total))

## Data Table
width=8
print(' decimal      hex   binary')
print('-'*27)
for num in range(1,16):
    for base in 'dXb':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

### References #################################################################
# - PDF Version of this 
#   - https://appacademy-open-assets.s3-us-west-1.amazonaws.com/Modular-Curriculum/content/python/topics/structures/assets/python-format-reference.pdf
# - Python Documentation on Formatted Output
#   - https://docs.python.org/3/library/string.html#formatspec
################################################################################
# capitalize() - Capitalize first letter of each word
print('mike'.capitalize())

# casefold() - Convert to lowercase. This is useful for matching strings.
#  - This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
print('MIKE'.casefold())

# center() - Returns a centered string of length width.
# center(width[, fillchar])
print('Mike'.center(20, 'x'))

# count() - Returns the number of non-overlapping occurrences of substring
# count(substring[, start[, end]])
print('Banananana'.count('na', 4, 6))

# endswith() - Returns True if the string ends with the specified suffix
# endswith(suffix[, start[, end]])
print('Mike'.endswith('ke'))

# expandtabs() - Expands tab characters to spaces
# expandtabs(tabsize)
print('Mike\tMike'.expandtabs(4))

# find() - Returns the lowest index in the string where substring is found 
#  - returns -1 if not found. 
#  - The find() method is almost the same as the index() method, the only    
#     difference is that the index() method raises an exception if the value is 
#     not found
# find(substring[, start[, end]])
print('Mike'.find('i'))

# format() - Formats specified values in a string, insert with `{#}`
# format(value[, format_spec])
print('{1} {0}'.format('Mike', 'Shuff'))

# index() - Returns the lowest index in the string where substring is found
# index(substring[, start[, end]])
print('Mike'.index('i'))
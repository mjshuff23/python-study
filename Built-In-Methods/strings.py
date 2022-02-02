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

# isalnum() - Returns True if all characters in the string are alphanumeric
# 'string'.isalnum()
print('Mike'.isalnum())

# isalpha() - Returns True if all characters in the string are in the alphabet
# 'string'.isalpha()
print('Mike'.isalpha())

# isascii() - Returns True if all characters in the string are ASCII
# 'string'.isascii()
print('Company123'.isascii())

# isdecimal() - Returns True if all characters in the string are decimal
# 'string'.isdecimal()
print('Mike'.isdecimal())
print('15'.isdecimal())

# isdigit() - Returns True if all characters in the string are digits
# 'string'.isdigit()
print('123a'.isdigit())

# isidentifier() - Returns True if the string is an identifier
#  - A string is considered a valid identifier if it only contains alphanumeric 
#     letters (a-z) and (0-9), or underscores (_). A valid identifier cannot 
#     start with a number, or contain any spaces.
# 'string'.isidentifier()
print('Mike'.isidentifier())

# islower() - Returns True if all cased characters in the string are lowercase
# 'string'.islower()
print('Mike'.islower())

# isnumeric() - Returns True if all characters in the string are numeric
#   - Exponents, like ² and ¾ are also considered to be numeric values.
#   - "-1" and "1.5" are NOT considered numeric values, because all the 
#      characters in the string must be numeric, and the - and the . are not.
# 'string'.isnumeric()
print('Mike'.isnumeric())

# isprintable() - Returns True if all characters in the string are printable
# 'string'.isprintable()
print('Mike'.isprintable())

# isspace() - Returns True if all characters in the string are whitespace
# 'string'.isspace()
print('Mike'.isspace())

# istitle() - Returns True if the string follows the rules of a title
# 'string'.istitle()
print('Mike'.istitle())

# isupper() - Returns True if all cased characters in the string are uppercase
# 'string'.isupper()
print('Mike'.isupper())

# join() - Joins the elements of an iterable to the end of the string
# 'string'.join(iterable)
print('-'.join(['Mike', 'Shuff']))

# ljust() - Returns a left justified version of the string
# 'string'.ljust(width[, fillchar])
print('Mike'.ljust(20, 'x'))

# lower() - Converts a string into lower case
# 'string'.lower()
print('Mike'.lower())

# lstrip() - Returns a left trim version of the string
# 'string'.lstrip([chars])
#  - chars - if specified, only characters in chars will be removed
print('   Mike'.lstrip('Mi '))

# maketrans() - Returns a translation table to be used in translations
# 'string'.maketrans(frm, to)
#  - frm - a string of characters to be translated
#  - to - a string of characters to replace the frm characters
my_translation = 'Mike'.maketrans('M', 'S')

# translate() - Translates a string using a translation table
# 'string'.translate(table)
print('Mike'.translate(my_translation))

# partition(separator) - Splits the string at the first occurrence of separator, and returns a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, returns a 3-tuple containing the string itself, followed by two empty strings.
# 'string'.partition(separator)
print('Mike'.partition('i'))

# replace() - Replaces all occurrences of old with new in the string
# 'string'.replace(old, new[, count])
print('Mikie'.replace('i', 'S'))

# rfind() - Returns the highest index in the string where substring is found
#  - returns -1 if not found.
# 'string'.rfind(substring[, start[, end]])
print('Mikie'.rfind('i'))

# rindex() - Returns the highest index in the string where substring is found
#  - raises an exception if not found
# 'string'.rindex(substring[, start[, end]])
print('Mikie'.rindex('i'))

# rjust() - Returns a right justified version of the string
# 'string'.rjust(width[, fillchar])
print('Mike'.rjust(20, 'x'))

# rpartition() - Splits the string at the last occurrence of separator, and returns a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, returns a 3-tuple containing two empty strings, followed by the string itself.
# 'string'.rpartition(separator)
print('Mikie'.rpartition('i'))

# rsplit() - Splits the string at the last occurrence of separator, and returns a list containing the string itself, followed by the separator, followed by any extra trailing substring
# 'string'.rsplit(separator[, maxsplit])
print('Mike'.rsplit('i'))

# rstrip() - Returns a right trim version of the string
# 'string'.rstrip([chars])
#  - chars - if specified, only characters in chars will be removed
print('Mike   '.rstrip())

# split() - Splits the string at the first occurrence of separator, and returns a list containing the string itself, followed by any extra trailing substring
# 'string'.split(separator[, maxsplit])
#  - separator - the separator to split on
#  - maxsplit - the maximum number of splits to do
print('Mike'.split('i'))

# splitlines() - Splits the string at line breaks and returns a list of the lines in the string
# 'string'.splitlines([keepends])
#  - keepends - if true, line breaks are included in the resulting list
print('Mike\nMike'.splitlines())

# startswith() - Returns True if the string starts with the prefix
# 'string'.startswith(prefix[, start[, end]])
print('Mike'.startswith('M'))

# strip() - Returns a trimmed version of the string
# 'string'.strip([chars])
print('Mike   '.strip())

# swapcase() - Swaps the case of all cased characters in the string
# 'string'.swapcase()
print('Mike'.swapcase())

# title() - Converts the first character of each word to upper case
# 'string'.title()
print('Mike'.title())

# upper() - Converts the string to uppercase
# 'string'.upper()
print('Mike'.upper())

# zfill() - Fills the string with a specified number of 0s on the left
# 'string'.zfill(width)
print('Mike'.zfill(20))
print('single quotes')
print("double quotes")
print('they\'re known as escape characters')
print("""Multi
Line
Strings""")
print(len('the length of this string is...'))

### INDEXING ####################################
print('Mike'[0]) # Indexing into a string
print('Mike'[1]) # Indexing into a string
print('Mike'[2]) # Indexing into a string
print('Mike'[3]) # Indexing into a string
print('Mike'[0:4]) # Using a range
print('Mike'[2:-1]) # Utilizing negative indexes
# A shortcut for the beginning of the string is to omit the first number.
print('Mike'[:-1])
# print('Mike'[5]) # Single indexes that don't exist will error out
print('Mike'[15:]) # Ranges do not

### STRING FUNCTIONS #############################
# index - returns the first position of a character
print('Mike'.index('k'))
# print('Mike'.index('3')) # If it doesn't exist in the string, it errors out

# count - How many times a substring appears in the string
print("Banana".count('na'))

# concatenation - Python uses the `+` to concatenate
#               - Multiply a string with `*`
print("hi"*5)
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
print("hi" + " " + "hi")
print("hi"*5)

# format()
#   - First, use placeholders in the string where you want the data to go. A 
#      placeholder is a number inside braces like this {0}. Start at zero and 
#      each placeholder gets the next number. The use the format function on
#      your string and pass in the data to substitute.
first_name = "Michael"
last_name = "Shuff"
print('Your name is {0} {1}'.format(first_name, last_name))
# For simple uses, a fast way to apply formatting is using the 'f' flag on the 
#  string. This means putting using single quotes with an f at the start.
print(f'Your name is {first_name} {last_name}')

# Other Useful Methods
print(first_name.upper()) # MIKE
print(first_name.lower()) # mike
print(first_name.isupper()) # false
print(first_name.islower()) # false
print(first_name.startswith('Mi')) # true
print(first_name.endswith('ael')) # true
full_name = "Michael Shuff"
print(full_name.split()) # ['Michael', 'Shuff']
print(full_name.split('h')) # ['Mic', 'ael S', 'uff']
names_array = ['Michael', 'Shuff']
print(' '.join(names_array)) # join() is on the string instead of the array

## Even More Methods
print('Mike'.isalpha()) # True if string consists of letters and is not blank
print('Mi234234'.isalnum()) # True is string consists of letters and numbers and is not blanks
print('23523523'.isdecimal()) # True is only numeric characters and not blank
print('    '.isspace()) # True if consists of only spaces, tabs, and new lines
print('Mike'.istitle()) # True if it is only words that begin capitalized
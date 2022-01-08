### FUNCTIONS ##################################################################
# - A function definition consists of
#   - The `def` keyword
#   - The `name` of the function
#   - A list of `parameters` to the function enclosed in parentheses, ()
#   - A colon, `:`, at the end of the line
#   - One tab indentation for the block of code to run (one or more lines)
def printCopyright():
    print("Copyright 2020. Me, myself and I. All rights reserved.")

### Parameters, Arguments, and Returning Values ################################
def average(num1, num2):
    return (num1/num2)

print(average(6, 2))        # => 3.0

### Default Parameter Values ###################################################
def greeting(name, saying="Hello"):
    print(saying, name)

greeting("Monica") # Hello Monica

greeting("Barry", "Hey") # Hey Barry

### Keyword Arguments ##########################################################
# - Unlike JavaScript, Python has the built-in ability to specify arguments by 
#    name without resorting to destructuring.
def greeting(name, saying="Hello"):
    print(saying, name)

greeting(name="Monica") # Hello Monica
greeting(name="Barry", saying="Hey") # Hey Barry
greeting(saying="Hey", name="Barry") # Hey Barry

### Anonymous Functions ########################################################
# - In JavaScript, you could just create functions and assign them to 
#    variables. Python has a special keyword, lambda, to allow you to create 
#    anonymous functions that you can assign to variables.
#
# - The so-called lambda functions in Python act like arrow functions in 
#    JavaScript. Lambda functions are meant to be one-line functions. 
#    Here is an example of uppercasing a string
toUpper = lambda s: s.upper()
print(toUpper('hello'))
################################################################################
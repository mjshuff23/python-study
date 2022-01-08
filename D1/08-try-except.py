##### TRY/EXCEPT ###############################################################
# - An error that occurs while a program is executing is called an exception
#
# - The process of detecting these execution errors is often referred to 
#    as catching exceptions.
#
# - The try...except blocks in Python work in a similar way to if...else. 
#    However there is nothing to check at the start. Instead try is like asking 
#    Python to listen for an error and do something with it other than crashing.
#
# - How about an example:
#   - For the purpose of this experiment, set a to an integer so you can see 
#      the error:
#      ```
#      a = 321
#      print(len(a))
#      ```
# Causes this output
#  - TypeError: object of type 'int' has no len()
a = 321
try:
    print(len(a))
except:
    print('Silently handle error here')
    # Optionally include a correction to the issue
    a = str(a)
    print(len(a))

### Naming Errors ####
a = 100
b = 0
try:
    c = a / b
except ZeroDivisionError:
    c = None
print(c)

### Handling Different Errors #### MUST COMMENT OUT ABOVE EXAMPLE FOR THIS
a = 100
# b = "5"
try:
    print(a / b)
except ZeroDivisionError:
    pass
except (TypeError, NameError):
    print("ERROR!")


### Else Clause #### This code will execute if no Error happens
# tuple of file names
files = ('01-intro.py', '02-numbers.py', '03-strings.sdfasdfaspy')

# simple loop
for filename in files:
    try:
        # open the file in read mode
        f = open(filename, 'r')
    except OSError:
        # handle the case where file does not exist or permission is denied
        print('cannot open file', filename)
    else:
        # do stuff with the file object (f)
        print(filename, 'opened successfully')
        print('found', len(f.readlines()), 'lines')
        # the variable f is available to use because it was successfully
        #  defined in the try block and no error occurred.
        f.close()

# Doing this without the else would take some tricky coding:
# tuple of file names
files = ('one.txt', 'two.txt', 'three.txt')

# simple loop
for filename in files:
    # CHANGE 1 or 2: Set f to none so we can check it later
    f = None
    try:
        # open the file in read mode
        f = open(filename, 'r')
    except OSError:
        # handle the case where file does not exist or permission is denied
        print('cannot open file', filename)
    
    # CHANGE 2 of 2: Check the value of f (None is equivalent to false)
    if f:
        # do stuff with the file object (f)
        print(filename, 'opened successfully')
        print('found', len(f.readlines()), 'lines')
        f.close()

### Finally ####################################################################
# - This is a clause designed to run clean-up actions in all circumstances.
#    That means whether an exception happened or not, the finally block will be 
#    executed. If present, finally will be the last task before the try 
#    statement completes.
#
# - If there is no except clause for a particular error, the finally block will 
#    run and then the exception will be re-raised.
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Result is", result)
    finally:
        print("Finally...")

divide(3, 0)
divide(0, 3)
divide(3, 1)

# If the finally block includes a return statement, then the returned value 
#  will come from finally, not try.

def greeting():
    try:
        return "Hey, friend."
    finally:
        return "Fun times!"

print(greeting())

# Checking for the existence of a property or method on an object may 
#  be performed with the hasattr function.

# Try a number - nothing will print out
a = 321
if hasattr(a, '__len__'):
    print(len(a))

# Try a string - the length will print out (4 in this case)
b = "5555"
if hasattr(b, '__len__'):
    print(len(b))
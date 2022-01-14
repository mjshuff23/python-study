###### FOR STATEMENTS ##########################################################
# In Python, there is only one for loop. In code, a for statement always  includes the following:
#   - The `for` keyword
#   - A variable name
#   - The `in` keyword
#   - An iterable of some kind
#   - A `colon`
#   - Starting on the next line, an indented block of code (called the for clause)

# The for loop in Python is very much like the for (..of..) loop in JavaScript. There is no counting version of the for loop in Python like the for(;;) version in JavaScript. Instead, you use the `range` function to create an iterable "filled" with numbers. The following sections show how to use the for loop with different kinds of iterables.

# Just like with the while loop, you can use break and continue statements inside for loops as well. The continue statement will continue to the next value of the for loop’s counter, as if the program execution had reached the end of the loop and returned to the start. In fact, you can use continue and break statements only inside while and for loops. If you try to use these statements elsewhere, Python will give you an error.
################################################################################
print('My name is')
for i in range(1, 6):
    print('Michael Shuff (' + str(i) + ')')

### With Lists #########
myList = ['a', 'b', 'what', 'ded']
for listItem in myList:
    print(listItem)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index: ' + str(i) + ' in the supplies is ' + supplies[i])
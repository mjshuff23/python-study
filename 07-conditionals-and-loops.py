##### CONDITIONALS AND LOOPS #########################
# `if` keyword
name = "Michael"

# keyword, condition, colon, indent
if name == "Michael":
    print("Hey, Michael")

# `else` keyword
if name == "John":
    print("Hey, John")
else:
    print("Not John")

# `elif` keyword chaining
if name == "John":
    print("Hey, John")
elif name == "Sofia":
    print("Hey, Sofia")
else:
    print("Not John OR Sofia")


### While Statements ######
spam = 0

while spam < 5:
    print('Hello, World')
    spam+=1

# Breaking out early
spam = 0

while True:
    print("Hello again, World")
    spam+=1
    if spam >= 5:
        break

# Continuing through an iteration
spam = 0

while spam <= 10:
    if spam % 2 == 1:
        spam+=1
        continue
    print(spam)
    spam+=1
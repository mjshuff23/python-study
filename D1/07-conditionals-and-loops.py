##### CONDITIONALS AND LOOPS #########################
name = "Michael"

# `if` keyword
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

### For Loops ####
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

### Range() Function ####
# Starts at 0
for x in range(6):
  print(x)

# With two arguments, the first argument is inclusive, the second is exclusive
for x in range(2, 6):
  print(x)

# With three arguments, the third is incrementing amount
for x in range(2, 30, 3):
  print(x)

# Else in a For loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
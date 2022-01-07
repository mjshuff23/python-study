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
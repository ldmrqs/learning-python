global_variables = "variables created outside of a function"
user_input = input("what are global variables? ")
if user_input == global_variables:
    print("you're correct, bro!")
else:
    print("keep trying, man.")

variable_same_name = "variable will be local, can only be used inside a function the global variable. the global variable with the same name will remain as it was, global and with the original value"
print(variable_same_name)
print("what the examples bellow:")

# global variables
favorite_band = "twenty one pilots"
def myfunc():
    print("my favorite band is " + favorite_band)
myfunc()

#variable inside a function with the same name as the global variable
Favorite_Band = "twenty one pilots"
def myfunc():
    Favorite_Band = "paramore"
    print("my favorite band is " + Favorite_Band)
myfunc()
print("my favorite band is " + Favorite_Band)

print("you can use the 'global' keyword to create a global variable inside a function")
def myfunc():
    global drummer
    drummer = "josh"
myfunc()
print("The drummer is " + drummer)

print("you can also use the global keyword to change a global variable inside a function")
singer = "tyler"
def myfunc():
    global singer
    singer = "josh"
myfunc()

print("The singer is " + singer)
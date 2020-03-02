# Basically, in a function, specify a variable is global if you want to access
# an already-defined global value, otherwise Python will just create another
# variable with the same name scoped to the function.
# WHICH ALSO MEANS - if you want to modify a global variable in a function, you have
# to use the global keyword.

# If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.
# If there is a global statement for that variable in a function, it is a global variable.
# Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
# But if the variable is not used in an assignment statement, it is a global variable.

def sayHelloWithoutGlobal(name):
    greeting = 'Local hi, '
    print(greeting + name)

def sayHelloWithGlobal(name):
    global greeting
    print(greeting + name)

greeting = 'Global hi, '
print('What''s your name?')

name = input()
sayHelloWithoutGlobal(name)
sayHelloWithGlobal(name)
testStr = "You can use double quotes with strings, \
    then you can use single quotes. Neat."

print(testStr)

testStr = 'You can also use escape characters. Here\'s a test.'
print(testStr)

print("How about newlines? \nDo those work, too?!")

print(r'Putting an 'r' before a string gives us raw string support.')

# Triple quote strings = multiline strings.
print('''Triple strings!

Look at this, no newlines or slashes or anything!

This ONLY works because tripe quotes means \"Multiline Strings\".''')

# Multi-line quotes!
"""
AH HA - this is how you do multi line quotes.

This doesn't generate any errors or look like a random string to track 
to Python. Neat.
"""

# Indexing and slicing works just like lists.
testStr = 'Hello, world!'
print('at position 3: ' + testStr[3])
print('slicing from 0 to 5: ' + testStr[0:5])
print('Slicing from -6: ' + testStr[-6:])

# So does "in" and "not in"
print('Hello' in testStr) # prints True
print('derp' in testStr) # prints False

# Putting strings inside other strings
# There's concatenating using the + operator:
hello = 'hello'
world = 'world'
testStr = hello + ' ' + world

# Or we can use string interpolation. %s for strings, then another % at
# the end with the variables being used.
testStr = '%s %s' %(hello, world)
print('Using Python-style interpolation: %s' %(testStr))

# OR, we can use f-strings. This is more like C# interpolation. Just stick
# an 'f' at the start of the string to tell Python to substitute the vars.
testStr = f'{hello} {world}'
print(f'Using f-string (C#-y) interpolation: {testStr}')



# Useful String Methods
#upper(), lower(), isupper(), islower().
# upper() and lower() don't modify the original string, just return the
# upper'd and lower'd versions of the string.
testStr = 'Hello, world!'
print('upper(): ' + testStr.upper())
print('lower(): ' + testStr.lower())
print('isupper(): ' + str(testStr.upper().isupper()))
print('islower(): ' + str(testStr.lower().islower()))

# "isX()" methods let you safely check if the string can be "cast" to
# another type, only consists of spaces or tabs, is a title, etc. Good
# for input validation.

# LEFT OFF AT startswith() and endswith()
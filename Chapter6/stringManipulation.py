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

# startswith() and endswith(). Case sensitive.
testStr = 'Hello, world. What\'s up?'
print('testStr = ' + testStr)
print('testStr.startswith(\'Hello\') = ' + str(testStr.startswith('Hello')))
print('testStr.startswith(\'hello\') = ' + str(testStr.startswith('hello')))

# join() and split() methods. For join, you start with the value you want
# to join everything with and then pass in the list of words you want to join.
testStr = ', '.join(['Hello', 'World'])
print(testStr)
testStr = 'DERP'.join(['Hello', 'World'])
print(testStr)

# split() is pretty straightforward. Defaults to splitting whitespace.
testList = 'This is a test list'.split()
print(testList)
# ... but we can split on anything.
testList = 'This is a test list.'.split('s')
print(testList)

# partition() splits a string into the text before and after a separator.
testStr = 'Hello, world!'
print(testStr.partition('world')) # spits back a 3 part list.


# Justifying text with rjust(), ljust(), and center().
# Give the amount of 'columns', and these methods will pad (whitespace by default)
print('Hello, world!'.ljust(40))
print('Hello, world!'.rjust(40))
print('Hello, world!'.center(40))
print('Hello, world!'.center(40, '*'))

# Remove whitespace with strip(), rstrip(), and lstrip(). Removes whitespace
# by default, but can again override that.
#! python3
# Input Validation

# Use the "as blah" so you can shorten to blah.whatever
import pyinputplus as pyip

# PyInputPlus: contains functions like input() that collect specific data, like
# phone numbers, email addresses, etc. It handles the input for you so you don't have to
# re-write the same things over and over.

"""
inputStr(): like input(), but you can pass custom validation to it.
inputNum(): only takes ints or floats.
inputChoice(): only accepts a pre-set list of choices.
inputMenu(): like inputChoice, but gives a menu with numbered or lettered options.
inputDatetime(): only accepts dates / times.
inputYesNo(): "yes" or "no"
inputBool(): "True" or "False", gives a bool.
inputEmail(): only accepts a valid email address.
inputFilepath(): accepts file paths, and can optionally ensure that the file exists.
inputPassword(): like "input()," but masks with *s as the user types.
"""

# If you don't input a number, it'll tell you it isn't a number and loop until you 
# do enter a legit number.
#response = pyip.inputNum()

# You can also send a string for a query to save on a "print()" call
#response = pyip.inputBool('Enter a bool here: ')

# Min, max, greaterThan, and lessThan Keyword arguments.
# Supported by inputNum, inputInt, and inputFloat.

# response = pyip.inputNum('Enter a number equal to or greater than 4: ', min = 4)
# print(f'You entered {response}')

# response = pyip.inputNum('Enter a number greater than 3 and less than 6: ', min = 3, max = 6)
# print(f'You entered {response}')

# response = pyip.inputNum('Enter a number less than 6, or nothing.', blank=True, lessThan=6)
#print(f'You entered {response}')

# You can use the limit arg to limit the amount of times a user is asked for a valid input.
# Can also use the timeout arg to set a limit for valid input in seconds.
# If either are violated they'll throw an exception
# try:
#     response = pyip.inputNum('Enter a number. You get two shots: ', limit=2)
# except Exception as ex:
#     response = f'How dare you...'
# print(response)

# allowRegexes and blockRegexes keyword arguments
# This will allow for numbers as well as roman numerals and the word "zero"
#response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

# Going the other way, use blockRegexes to not allow certain values.
# This will block anything that ends with an even number.
#response = pyip.inputNum(blockRegexes=[r'[02468]$'])

# Custom validation functions can be used. Basically an anonymous function.
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
    return int(numbers)

# Now pass the anon function to "inputCustom()". Note, don't use parens.
response = pyip.inputCustom(addsUpToTen)
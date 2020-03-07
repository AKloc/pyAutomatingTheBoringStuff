# Dictionaries, just using strings.
myCat = {'size': 'fat', 'color': 'gray', 'disposition':'loud'}
print('My cat has ' + myCat['color'] + ' fur.')

# Dictionaries can  use different types for keys or values.
luggage = {'color': 'black', 'combination': 12345}
luggage2 = {'color': 'brown', 12345: 'combination'}
print('My luggage is ' + luggage['color'] + ' and its combo is ' + str(luggage['combination']))
print('Your luggage is ' + luggage2['color'] + ' and 12345 is its ' + luggage2[12345])

# Main differences between dictionaries and lists:
#  - dictionaries aren't ordered (3.7 supports this with some extra work)
#  - dictionaries can't be sliced.

# You can check for keys being present like so:
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
if 'Alice' in birthdays:
    print('Alices birthday is ' + birthdays['Alice'])

# keys(), values() and items() methods

# values() pulls back all of the values of a dictionary.
spam = {'color': 'red', 'age':42}
for v in spam.values():
    print(v)
# keys pulls back all of the keys in the dictionary.
for k in spam.keys():
    print(k)

# items pulls back key AND value.
for i in spam.items():
    print(i)

# Getting fancier and pulling back keys and values separately...
for k, v in spam.items():
    print('Key is ' + k + ', value is ' + str(v))

# Does a key exist in the dictionary?
if 'color' in spam.keys():
    print('color is a key in spam.')
# Does a value exist in the dictionary?
if 42 in spam.values():
    print('42 is one of the values.')

# What if we want to grab a value but don't know if the key is in there?
# Instead of checking using the "in" keyword, just use "get" and it'll perform the check.
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# LEFT OFF AT "The setdefault() method"
# Used when you want to have a default value if the key doesn't have a value.
# BEFORE:
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

# AFTER:
spam = {'name': 'pooka', 'age': 5}
spam.setdefault('color', 'black')


# Nested dictionarlies and lists are a thing.

nestedDictionary = {'taylor': {'color': 'pink', 'age': 8}}
dictionaryOfDictionaries = {'taylor':{'color':'pink', 'age':48},
                            'alex':{'color':'blue', 'age':6}}

derp = 'derp'
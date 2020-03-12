#! python3

# "re" seems unfortunate to abbreviate to.
import re

# Start by "compiling" a regex object. \d means "digit". Note the 'r' in front.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# search() on the regex object looks to see if the string matches.
matchObject = phoneNumRegex.search('Here is my phone. 716-713-1171 is just that.')

print('Found phone number: \'' + matchObject.group() + '\'')
# gorup() will return None if there isn't a match.

""" General Regex Breakdown:
1. Import the regex module with "import re"
2. Create a Regex object using re.compile using a raw string
3. Pass the string to search on into the regex object's "search()" method.
4. Call the match object's "group()" method to return a string
"""

# What if we wanted to separate the area code from the rest of the number?
# Use groups - this is the same regex,but has parens.
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search('Here is my phone. 716-713-1171 is just that.')
print('matchObject.groups is size ' + str(len(matchObject.groups())))
print('First item: \'' + matchObject.group(1) + '\'')
print('Second item: \'' + matchObject.group(2) + '\'')

# How about getting the area code? Need to look for parens. Use escape character "\"
phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search('Here is my phone. (716)-713-1171 is just that.')
print('matchObject.groups is size ' + str(len(matchObject.groups())))

# These all have special meanings that need to be escaped:
#     .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )

# Matching multiple groups with pipes. The | works like an "or" and finds the first
# occurrence found.
heroRegex = re.compile(r'Batman|Tina Fey')
matchObject = heroRegex.search('Batman and Tina Fey')
print(matchObject.group())
matchObject = heroRegex.search('Tina Fey and Batman')
print(matchObject.group())

# You can find all matches with findall() 
allMatches = heroRegex.findall('Tina Fey and Batman and Tina Fey')
print('Found ' + str(len(allMatches)) + ' matches')

# Pipes also give you versatility.
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
matchObject = batRegex.search('Batmobile lost a wheel')
print(f'Found: {matchObject.group()}')
allMatches = batRegex.findall('Batmobile lost a wheel')
print(f'Found: {str(len(allMatches))} matches.')

# Optionally match on anything by putting a question mark after the parens.
batRegex = re.compile(r'Bat(wo)?man')
matchObject = batRegex.search('The adventures of Batman')
print(f'Found: {matchObject.group()}')
matchObject = batRegex.search('The adventures of Batwoman')
print(f'Found: {matchObject.group()}')

# Let's make the area code optional.
phoneNumRegex = re.compile(r'(\(\d\d\d\)-)?\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search('(555)-867-5309') # whole thing matches.
print(f'Found: {matchObject.group()}')
matchObject = phoneNumRegex.search('716-867-5309') # this matches just the phone num without area code
print(f'Found: {matchObject.group()}')

# Asterisk means "match zero or more". The group that comes before can occur any number of times.
batRegex = re.compile(r'Bat(wo)*man')
matchObject = batRegex.search('The Adventures of Batman') # Matches.
print(f'Match: {matchObject.group()}')
matchObject = batRegex.search('The Adventures of Batwoman') # Matches.
print(f'Match: {matchObject.group()}')
matchObject = batRegex.search('The Adventures of Batwowowowowoman') # Matches.
print(f'Match: {matchObject.group()}')
matchObject = batRegex.search('The Adventures of Batwdwdwdwdwdman') # DOESN'T match.
#print(f'Match: {matchObject.group()}')

# Plus means "match ONE or more." Works the same way as asterisk.
batRegex = re.compile(r'Bat(wo)+man')
matchObject = batRegex.search('The Adventures of Batman') # DOESN'T match.
#print(f'Match: {matchObject.group()}')
matchObject = batRegex.search('The Adventures of Batwoman') # Matches.
print(f'Match: {matchObject.group()}')
matchObject = batRegex.search('The Adventures of Batwowowowowoman') # Matches.
print(f'Match: {matchObject.group()}')
matchObject = batRegex.search('The Adventures of Batwdwdwdwdwdman') # DOESN'T match.
#print(f'Match: {matchObject.group()}')

# Can ALSO match on an exact number of repetitions. Same as + or *, use curly braces.
# Can use ranges here, too. e.g., {3,5} will match with 3,4,5 repetitions.
# {3,} matches 3 or more. {,5} will match 0 to 5.
batRegex = re.compile(r'Bat(wo){3,5}man')
matchObject = batRegex.search('The Adventures of Batman') # DOESN'T match.
#print(f'Match: {matchObject.group()}')
matchObject = batRegex.search('The Adventures of Batwoman') # DOESN'T match.
#print(f'Match: {matchObject.group()}')
matchObject = batRegex.search('The Adventures of Batwowowoman') # Matches.
print(f'Match: {matchObject.group()}')
matchObject = batRegex.search('The Adventures of Batwowowowowoman') # Matches.
print(f'Match: {matchObject.group()}')

# Greedy and non-greedy matching...

# search(): returns a Match object of the FIRST matched text in the searched string.
# findall(): return the strings of every match.

"""
Character classes:
\d: digits, 0-9
\D: any character that ISN'T A digit, 0-9
\w: any letter, digit, or underscore. The w is basically for "word."
\W: anything NOT a \w.
\s: space characters. Spaces, tabs, newlines.
\S: anything NOT a \s.

You can make your own character classes, too...
"""

# Creating a custom character class.
vowelRegex = re.compile(r'[aeiouAEIOU]')
# And going the other way - use a carat and pick every non-vowel.
nonVowelRegex = re.compile(r'[^aeiouAEIOU]')

# The caret and dollar sign characters:
# Using a ^ at the start of a regex shows that a match has to have this at the beginning.
# Using a $ at the end of a regex means that a match has to have this at the end.

beginsWithHello = re.compile(r'^Hello')
searchResult = beginsWithHello.search('Hello, world!')
print(f'Found {searchResult}') # Finds a match.
# Let's see if it works if 'Hello' isn't at the beginning.
searchResult = beginsWithHello.search('Hey world. Hello.')
print(f'Found {searchResult}') # DOESN'T match.

endsWithNumber = re.compile(r'\d$')
searchResult = endsWithNumber.search('Here\'s a test.')
print(f'Found {searchResult}')
# Now try with a number.
searchResult = endsWithNumber.search('Here\'s a test. 1')
print(f'Found {searchResult}')

# The below basically means "starts and ends with one or more digits"
wholeStringIsNum = re.compile(r'^\d+$')

# Wildcard character "." will match on anything that isn't a newline.
atRegex = re.compile(r'.at')
searchResult = atRegex.findall('The cat in the hat sat on the flat mat.')
print(f'Found {str(len(searchResult))} matches.')

# Match everything with .*
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
searchResult = nameRegex.findall('First Name: Andy Last Name: Kloc')
print(f'Found {str(len(searchResult))} matches.')
print(searchResult)

# Ignore case by passing an ignore case parameter to the compile method:
ignoreCaseRegex = re.compile(r'HeRe Is TeXT: .*', re.I) # re.IGNORECASE also works here.
searchResult = ignoreCaseRegex.findall('here is text: Hello.')
print(f'Found {str(len(searchResult))} matches.')
print(searchResult)

# Substitute strings on matches with sub()
namesRegex = re.compile(r'Agent \w+')
afterSubs = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(afterSubs)
agentNamesRegex = re.compile(r'Agent (\w)\w*')
afterSubs = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent \
Eve knew Agent Bob was a double agent.')
print(afterSubs)

# STOPPED AT Managing Complex Regexes

"""
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.
"""
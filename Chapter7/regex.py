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

# STOPPED AT MATCHING MULTIPLE GROUPS WITH PIPES
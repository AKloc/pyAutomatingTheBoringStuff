#! python3

# "re" seems unfortunate to abbreviate to.
import re

# Start by "compiling" a regex object. \d means "digit". Note the 'r' in front.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
value = phoneNumRegex.search('Here is my phone. 716-713-1171 is just that.')
print(value.group())

# search() looks to see if the string matches.
# STOPPED AT "Matching Regex Objects"
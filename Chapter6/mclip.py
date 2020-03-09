#! python3
# mclip.py - A multi-clpipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  # the first command line arg is the keyphrase.
print('Saw argument: ' + keyphrase)

""" 
Check to see if value exists. If it does, copy the text to the clipboard.
Use pyperclip.copy().
"""

if keyphrase in TEXT.keys():
    print('Got the key! Copying: ' + TEXT[keyphrase])
    pyperclip.copy(TEXT[keyphrase])
else:
    print('Sorry, don\'t have that key.')
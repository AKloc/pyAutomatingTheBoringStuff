#! python3
# That line is called the "shebang" line. It tells the computer what program
# or interpreter to use to run the script. It's a Linux thing.

"""The bulletPointAdder.py script will get the text from the clipboard, 
add a star and space to the beginning of each line, and then paste this
new text to the clipboard."""

import pyperclip

rawText = pyperclip.paste()
# Add a star and space to the beginning of each line.
rawTextLines = rawText.split('\n')
for i in range(len(rawTextLines)):
    rawTextLines[i] = '* ' + rawTextLines[i]

# Join back up.
output = '\n'.join(rawTextLines)
print('Copying output: ' + output)
pyperclip.copy(output)
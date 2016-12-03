#bulletPointAdder.py - Adds wikipedia bullet points to the start
#of each line of the text on the clipboard

import pyperclip
text = pyperclip.paste()
#Separate lines and add stars
lines = text.split('\n')

#loop through all indexes in the "lines" list
for i in range(len(lines)): 
#add star to each string in "lines" list
	lines[i] = '*' + lines[i] 

#the pyperclip.copy can not do copy with list so use join method to
#make a string again.
text = '\n'.join(lines)
pyperclip.copy(text)
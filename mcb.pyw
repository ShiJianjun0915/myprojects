# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: 
# python3 mcb.pyw save <keyword> - Saves clipboard to keyword.
# python3 mcb.pyw save <keyword> - Loads keyword to clipboard.
# python3 mcb.pyw list - Loads all keywords to clipboard.
# python3 mcb.pyw delete <keyword> - delete the keyword.
# python3 mcb.pyw delete - delete the all keywords

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
	# Save clipboard content
	if sys.argv[1].lower() == 'save' sys.argv[2] in mcbShelf:
		mcbShelf[sys.argv[2]] = pyperclip.paste()
	#delete the keyword
	elif sys.argv[1].lower == 'delete' and sys.argv[2] in mcbShelf:
		del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
	elif sys.argv[1].lower() == 'delete':
		mcbShelf.clear()
mcbShelf.close()
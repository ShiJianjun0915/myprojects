#This project uses dictionary to keep the accounts and the passwords
#when run the code, use python3 passwordLocker.py account and get its
# password copied to the clipboard, the passwordLocker is not secure
import sys, pyperclip

PASSWORDS = {'email': 'emailpassword12', 'blog': 'blogpassword12',
'luggage': 'luggagepassword12'}

if len(sys.argv) < 2:
	print('Usage: py passwordLocker.py [account]\
	 - copy account password')
	sys.exit()

account = sys.argv[1] # first command line arg is the account name
if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for '+ account + ' copied to clipboard.')
else:
	print('There is no account named ' + account + '.')
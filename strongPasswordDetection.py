'''Write a function that uses regular expressions to make sure
the password string it is passed is strong. A strong password
is defined as one that is at least eight characters long, 
contains both uppercase and lowercase characters, and has
at least one digit. You may need to test the string against
multiple regex patterns to validate its strength.
'''
import re

capReg = re.compile(r'.*[A-Z].*')
lowerReg = re.compile(r'.*[a-z].*')
digitReg = re.compile(r'.*\d.*')


def checkPassword(text):
	if len(text) < 8:
		return False
	if (capReg.search(text) and lowerReg.search(text)\
	 and digitReg.search(text)):
		return True
	else:
		return False

password1 = '123qWE'
password2 = '12343QAp'
print('password1 is a strong password:')
print(checkPassword(password1))
print('password2 is a strong password:')
print(checkPassword(password2))
import re

fileRegex = re.compile('ADJECTIVE|NOUN|VERB')
fhand = open('madLibs.txt')
fileContent = fhand.read()
fhand.close()
print(fileContent)

adj = input('Enter an abjective:\n')
firstNoun = input('Enter a noun:\n')
verb = input('Enter a verb:\n')
secondNoun = input('Enter a noun:\n')

words = [adj, firstNoun, verb, secondNoun]

for i in range(len(words)):
	fileContent = fileRegex.sub(str(words[i]), fileContent, count = 1)

print(fileContent)

file = open('madLib.txt',  'w')
file.close()
import re

fhand = open('madLibs.txt')
fileContent = fhand.read()
print(fileContent)
fhand.close()
fileRegex = re.compile('ADJECTIVE|NOUN|VERB')

print('Enter an adjective:')
adj = input()
fileContent = fileRegex.sub(adj, fileContent, count = 1)
#print(fileContent)

print('Enter a noun:')
nounFst = input()
fileContent = fileRegex.sub(nounFst,fileContent, count=1 )

print('Enter a verb:')
verb = input()
fileContent = fileRegex.sub(verb,fileContent, count = 1)

print('Enter a noun:')
nounScd = input()
fileContent = fileRegex.sub(nounScd, fileContent, count = 1)
print(fileContent)

file = open('madLibs.txt', 'w')
file.write(fileContent)
file.close()print(fileContent)
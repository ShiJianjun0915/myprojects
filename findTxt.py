import re, os

fileNameRegex = re.compile('\.txt$')
fileNames = os.listdir('/home/jianjun/learnpycode')
txtFileNames = []

for i in range(len(fileNames)):
	if not fileNameRegex.search(fileNames[i]):
		continue
	txtFileNames.append(fileNames[i])
print(txtFileNames)

for j in range(len(txtFileNames)):
	txtFile = open('/home/jianjun/learnpycode/%s' 
		%txtFileNames[j])
	txtContent = txtFile.read()
	print(txtContent+ '\n')
	txtFile.close()
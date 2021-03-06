'''
Write a function named printTable() that takes a 
list of lists of strings and displays it in a well-
organized table with each column right-justified. 
Assume that all the inner lists will contain the 
same number of strings.
'''
tableData = [['apples', 'oranges', 'cherries', 'banana'],
			['Alice', 'Bob', 'Carol', 'David'],
			['dogs', 'cats', 'moose', 'goose']]

def printTable(tableList):
	lengthList = []
	length = 0
	for i in range(len(tableList)):
		for j in range(len(tableList[i])):
			if length <= len(tableList[i][j]):
				length = len(tableList[i][j])
		lengthList.append(length)

		length = 0

	for j in range(len(tableList[0])):
		for i in range(len(tableList)):
			width = lengthList[i]
			print(tableList[i][j].rjust(width), end = ' ') 
		print()
		
printTable(tableData)
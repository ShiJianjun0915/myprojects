# My main idea is to copy the file name which is not in right,
# and rename it, then delete it.

import os, shutil


# Arguments: folder, prefix
def fillGap(folder,prefix):

	# Makee sure the path is absolute.
	folder = os.path.abspath(folder)
	# Change the path which have the files.
	os.chdir(folder)
	# Make a list to contain the file with prefix.
	fileNames = list()
	for filename in os.listdir(folder):
		if filename.startswith('spam') and filename.endswith('.txt'):
			fileNames.append(filename)
	fileNames.sort()
	print(fileNames)

	# Find the gap through incremting loops
	for i in range(len(fileNames)):
		if int(fileNames[i].lstrip('spam').rstrip('.txt')) == i + 1:
			continue
		# Rename the old one then delete it.
		newOrder = str('{:0>3}'.format(i + 1))
		print(fileNames[i] + '-->' + prefix + newOrder + '.txt')
		shutil.copy(fileNames[i], prefix + newOrder + '.txt')
		os.unlink(fileNames[i])

folder = '/home/jianjun/spam'
prefix = 'spam'
fillGap(folder, prefix)
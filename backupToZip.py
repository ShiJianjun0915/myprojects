# backupToZip.py - Copies an entire folder and its contents into
# a Zip file whose filename increments.

import zipfile, os

def backupToZip(folder):
	# Backup the entire contents of "folder" into a ZIP file.

	# Make sure folder is absolute.
	folder = os.path.abspath(folder)

	# Figure out the filename this code should use based on what
	# files already exist.
	number = 1
	while True:
		zipFileName = os.path.basename(folder) + '-' + str(number) \
		+ '.zip'
		if not os.path.exists(zipFileName):
			break
		number = number + 1

	# Create the ZIP file.
	print('Creating %s... ' % (zipFileName))
	backupZip = zipfile.ZipFile(zipFileName, 'w')

	# Walk the entire folder tree and compress the files in each 
	#folder.
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding files in %s...' % (foldername))

		# Add the current folder to the ZIP file.
		backupZip.write(foldername)

		#Add all files in this folder to the ZIP file.
		for filename in filenames:
			newBase  = os.path.basename(folder) + '-'
			if filename.startswith('newBase') and filename.endswith('.zip'):
				continue # don't backup the backup ZIP files
			backupZip.write(os.path.join(foldername, filename))
	backupZip.close() 
	print('Done.')
backupToZip('/home/jianjun/capitalQuiz')
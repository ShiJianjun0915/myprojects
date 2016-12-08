import os, send2trash

foldername = '/'
for foldername, subfolders, filenames in os.walk(foldername):
	for filename in filenames:
		if filename.endswith('.pdf'):
			try:
				send2trash.send2trash(os.path.join(foldername,
				 filename))
				print(os.path.join(foldername,filename))
			except:
				continue


print('Done')
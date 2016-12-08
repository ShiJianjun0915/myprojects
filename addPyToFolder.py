import os, shutil

try:
	os.mkdir('/home/jianjun/pyfile')
except:
	pass
folder = '/'
count = 0
for foldername, subfolders, filenames in os.walk(folder):

	for filename in filenames:
		if filename.endswith('.py'):
			if os.path.exists(os.path.join('/home/jianjun/pyfile', filename)):
				continue
			shutil.copy(os.path.join(foldername, filename),
			 '/home/jianjun/pyfile')
			count = count + 1

print('Done')
print('Count = %s' % count)
import os
import shutil
import datetime

#List of directories from where you want to backup
source_dirs = []#Fill the list with the paths pf the directories or folders you want to backup
#eg: source_dirs = ['/storage/emulated/0/Documents/Text Editor','/storage/emulated/0/New folder','/storage/emulated/0/Download/Cam Scanner']

#Directory where the backup data to be storef
destination_dir = ''#Path of the directory or folder where you want to backup
#eg: destination_dir = '/storage/emulated/0/Notifications'

def copy_folder_to(source,dest):
	list = os.listdir(dest)#To get the list of all the directories in the destination directory
	
	if len(list) != 0:#Checks if directory is empty or not
	    for item in list:
	    	remove_dir = os.path.join(dest,item)#To get the path of the directory to be removed
	    	shutil.rmtree(remove_dir)#To remove the previous directories in the destination directory

	today = datetime.date.today()
	for item in source:
		char = '/'
		pos = item.rfind(char)
		
		dest_dir = os.path.join(dest,str(today)+' ' + item[pos + 1:])#creates the path for the new directory in the destination directory
		
		#Name of new directory will be...eg - '2024-03-05 Screenshots'(along with the name of source directory)
		
		try:
			shutil.copytree(item,dest_dir)#copies recursively all contents in source to the dest dir
			print(f'Folder copied to {dest_dir}')
		except FileExistsError:
			print('folder already exists')
		except PermissionError:
			print('Permission required..Backup unsuccessfull')
		except OSError:
			print('Invalid Directory or its properties')

copy_folder_to(source_dirs,destination_dir)
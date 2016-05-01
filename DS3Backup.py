'''
DS3Backup
By Charles Laymon
chucklay@yahoo.com

This is a simple script to backup Dark Souls 3 saves.
This script also rotates save files to keep multiple backups.

'''

import time
import pickle
import win32ui
import subprocess
import DS3BackupConfig
from shutil import copyfile

currentSave = 1;

try:
	with open('data.p', 'rb') as data:
		currentSave = pickle.load(data)
		print('Detected previous use. Resuming from last save slot.')
except IOError:
	print('No previous run detected. Defaulting to first save.');

print('Attempting to launch Dark Souls III...');

subprocess.call(DS3BackupConfig.gamePath);					#Launch DS3.

time.sleep(60);									#Wait a minute to make sure the game has time to launch.

while(True):
	copyfile(DS3BackupConfig.source, DS3BackupConfig.dest + \
			'DS3BACKUP_' + str(currentSave) + '.sl2')		#Copy the save file
	print('Save file backed up to slot ' + str(currentSave) + '.')
	currentSave += 1
	if(currentSave > DS3BackupConfig.maxSave):
		currentSave = 1;						#Loop back to 1 if the max save file has been reached.
	with open('data.p', 'wb') as data:
		pickle.dump(currentSave, data)					#Dump the current save file for later runs.

										#Check to see if DS3 is still running. If not, exit.
	try:
		win32ui.FindWindow(None, 'DARK SOULS III')
	except win32ui.error:
		print('Dark Souls does not appear to be running. Exiting...')
		quit();
	
	print('Waiting to to preform next backup.')
	time.sleep(DS3BackupConfig.interval * 60)				#Wait a user-defined amount of time before next execution.

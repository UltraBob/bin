#!/usr/bin/python

import os
import subprocess
import sys
import smtplib
from pyunpack import Archive
from email.mime.text import MIMEText

""" TODO:

"""
if len(sys.argv) > 1: # if a path is provided as an argument, use the directory path as the starting point
	if os.path.exists(sys.argv[1]):
		if os.path.isfile(sys.argv[1]):
			start_path = os.path.dirname(sys.argv[1])
		else:
			start_path = sys.argv[1]
	else:
		start_path = os.getcwd()
else:
	start_path = os.getcwd()
print "start path is " + start_path
try:
    from vidhunter_config import *
except ImportError:
    pass
arch_files = []

for root, dirs, files in os.walk(start_path):
	for name in files:
		for extension in archive_extensions:
			if name.lower().endswith(extension):
				arch_files.append(os.path.join(root, name))
if len(arch_files) > 0:
	print ("files to unzip: ", arch_files)
	for file in arch_files:
		Archive(file).extractall(os.path.dirname(file))
	
vidwalk=[]
rmwalk=[]

for (root, dirs, files) in os.walk(start_path, topdown=False): # create a snapshot of currently folder and file situation to work with to avoid deleting late additions
    rmwalk.append((root,dirs,files))

for (root, dirs, files) in os.walk(start_path): # create a snapshot of currently folder and file situation to work with to avoid deleting late additions
    vidwalk.append((root,dirs,files))

if len(vidwalk) == 1 and (len(vidwalk[0][2]) == 0 or (len(vidwalk[0][2]) == 1 and vidwalk[0][2][0] == ".DS_Store")): # if there are no files and/or subdirectories
    print "No files found, exiting"
    exit()

vidfiles = []
for root, dirs, files in vidwalk:
   for name in files:
   	for extension in extensions:
   		if name.lower().endswith(extension):
   			vidfiles.append(os.path.join(root, name))
   			
if len(vidfiles) == 0: #if no video files were found send an e-mail
	mailmessage = "These are the files that are included:\r\n\r\n"
	for root, dirs, files in vidwalk:
		mailmessage += "\r\nIn" + str(root) + "/" + str(dirs) + ": " + str(files) + "\r\n"
	mailmessage += "\r\n\r\nthese remain in place until next time the script runs and finds a video."
	print (mailmessage)
	msg = MIMEText(mailmessage)
	msg['Subject'] = "The vidhunter script failed because it didn't find any videos"
	msg['From'] = email_address
	msg['To'] = email_address
	s = smtplib.SMTP('localhost')
	s.sendmail(email_address, email_address, msg.as_string())
	s.quit()
	sys.exit()
	
vidfiles.insert(0,'/Users/moko/bin/converttotvcast.sh')
print("vidfiles: ",vidfiles)
subprocess.check_call(vidfiles)

for root, dirs, files in rmwalk:
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))


print "done!"

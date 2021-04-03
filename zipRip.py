#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time
import zipfile
import random
import string

class bc:
	GC = '\033[1;39m'
	BC = '\033[1;34m'
	RC = '\033[1;31m'

author = bc.BC + "\n Author: " + bc.RC + "4" + bc.GC + "x" + bc.BC + "x" + bc.RC + "4" + bc.GC + "0" + bc.BC + "4\n"
version = bc.BC + " Version: " + bc.RC + "1" + bc.GC + "." + bc.BC + "0\n"
github = bc.BC + " Github: " + bc.RC + "h" + bc.GC + "t" + bc.BC + "t" + bc.RC + "p" + bc.GC + "s" + bc.BC + ":" + bc.RC + "/" + bc.GC + "/" + bc.BC + "g" + bc.RC + "i" + bc.GC + "t" + bc.BC + "h" + bc.RC + "u" + bc.GC + "b" + bc.BC + "." + bc.RC + "c" + bc.GC + "o" + bc.BC + "m" + bc.RC + "/" + bc.GC + "4" + bc.BC + "x" + bc.RC + "x" + bc.GC + "4" + bc.BC + "0" + bc.RC + "4\n"

banner = bc.RC + '''
                (                
''' + bc.GC + '''                )\ )             
''' + bc.BC + '''     (         (()/( (           
''' + bc.RC + '''  (  )\   ) )   )(_)))\   ) )    
''' + bc.GC + '''  )\((_) /(/(  (_)) ((_) /(/(    
''' + bc.BC + ''' ((_)(_)((_)_\ | _ \ (_)((_)_\   
''' + bc.RC + ''' |_ /| || '_ \)|   / | || '_ \)  
''' + bc.GC + ''' /__||_|| .__/ |_|_\ |_|| .__/   
''' + bc.BC + '''        |_|             |_|      
''' + author + version + github

iBan = bc.BC + " [" + bc.GC + "?" + bc.BC + "]"
sBan = bc.BC + " [" + bc.GC + u'\u2713' + bc.BC + "]"
eBan = bc.BC + " [" + bc.RC + u'\u2717' + bc.BC + "]"

clr = 'clear'  
os.system(clr)
print(banner)

def zipRip():
	try:
		wordlist = str(input(bc.BC + ' Password Wordlist: ' + bc.GC))
		if(wordlist == ''):
			os.system(clr)
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Password Wordlist value cannot be empty\n')
			time.sleep(1)
			zipRip()
		else:
			pass
	except KeyboardInterrupt:
		os.system(clr)
		print(banner)
		print(bc.BC + ' Closing zipRip...')
		time.sleep(1)
		os.system(clr)
		print(banner)
		quit()

	try:
		zipFile = str(input(bc.BC + ' Zip File: ' + bc.GC))
		if(zipFile == ''):
			os.system(clr)
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Zip File value cannot be empty\n')
			time.sleep(1)
			zipRip()
		else:
			pass
	except KeyboardInterrupt:
		os.system(clr)
		print(banner)
		print(bc.BC + ' Closing zipRip...')
		time.sleep(1)
		os.system(clr)
		print(banner)
		quit()

	try:
		passwords = open(wordlist, 'rb')
	except Exception:
		os.system(clr)
		print(banner)
		print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Failed to open Password Wordlist: ' + bc.RC + wordlist + '\n')
		time.sleep(1)
		zipRip()

	tries = 1
	
	try:
		if(zipFile.endswith('.zip')):
			dirName = zipFile.split('.')[0]
			zipExtractPath = 'extracted/' + dirName
			fileDATA = []
			for word in passwords:
				os.system(clr)
				print(banner)
				passwd = word.strip()
				triesBanner = bc.BC + ' [' + bc.GC + str(tries) + bc.BC + ']'
				try:
					print(bc.BC + triesBanner + ' Trying Password: ' + bc.GC + str(passwd.decode('utf-8')))
					with zipfile.ZipFile(zipFile, 'r') as zf:
						zf.extractall(path=zipExtractPath, pwd=passwd)
						data = zf.namelist()
						for d in data:
							data_size = zf.getinfo(d).file_size
							fileinfo = str(d) + ':#:' + str(data_size) + 'kb' 
							fileDATA.append(fileinfo)
						break
				except Exception:
					print(eBan + bc.RC + ' ' + str(passwd.decode('utf-8')))
					time.sleep(0.1)
					tries += 1
					continue

			os.system(clr)
			print(banner)
			print(bc.BC + ' Password Wordlist: ' + bc.GC + wordlist)
			print(bc.BC + ' Zip File: ' + bc.GC + zipFile)
			print('\n' + sBan + ' Password Found: ' + bc.GC + str(passwd.decode('utf-8')))
			print(bc.BC + '\n Contents Information:')
			for dat in fileDATA:
				file = dat.split(':#:')[0]
				size = dat.split(':#:')[1]
				print('\t' + sBan + ' File: ' + bc.GC + str(file))
				print('\t' + sBan + ' Size: ' + bc.GC + str(size) + '\n')

		else:
			os.system(clr)
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + zipFile + bc.BC + ' does not have a .zip extension\n')
			time.sleep(1)
			zipRip()
	except KeyboardInterrupt:
		print(bc.BC + '\n Stopping zipRip Cracker...\n')
		time.sleep(1)
		input(bc.BC + ' Press Enter to Continue...')
		os.system(clr)
		print(banner)
		zipRip()

if __name__ == '__main__':
	zipRip()

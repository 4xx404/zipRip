#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time, zipfile
sys.dont_write_bytecode = True

from Core.Stylesheet.Styling import sd, bc
from Core.Console import Console
from Core.Commands import Command
from Core.Validity import Validation

class ZipRip:
	def __init__(self):
		self.Console = Console()
		self.Cmd = Command()
		self.Validator = Validation()

		self.Wordlist = ""
		self.ZipFile = ""
		self.ExtractToPath = ""
		self.Passwords = []

		self.Tries = 1
		self.FoundPassword = ""
		self.ResponseData = []

	def SetWordlist(self):
		Wordlist = str(input(f"{bc.BC} Password Wordlist: {bc.GC}"))

		if (not self.Validator.NotEmpty(Wordlist)):
			self.Cmd.Clear(f"{sd.eBan}{bc.BC} Password wordlist is required\n", True)

		elif (not os.path.isfile(Wordlist)):
			self.Cmd.Clear(f"{sd.eBan}{bc.BC} No wordlist named {bc.RC}{Wordlist}{bc.BC} exists\n", True)

		self.Wordlist = Wordlist

	def SetZipFile(self):
		ZipFile = str(input(f"{bc.BC} Zip File: {bc.GC}"))

		if(not self.Validator.NotEmpty(ZipFile)):
			self.Cmd.Clear(f"{sd.eBan}{bc.BC} Zip File is required\n", True)

		elif (not ZipFile.endswith(".zip")):
			self.Cmd.Clear(f"{sd.eBan}{bc.BC} file {bc.RC}{ZipFile}{bc.BC} is not a .zip file", True)

		elif (not os.path.isfile(ZipFile)):
			self.Cmd.Clear(f"{sd.eBan}{bc.BC} no zip file named {bc.RC}{ZipFile}{bc.BC} exists\n", True)

		self.ZipFile = ZipFile

	def SetZipFileDirectory(self):
		if (not self.Validator.NotEmpty(self.ZipFile)):
			self.Cmd.Clear(f"{sd.eBan}{bc.BC} could not establish zip file directory", True)

		self.ExtractToPath = os.path.splitext(os.path.basename(self.ZipFile))[0]

	def SetPasswords(self):
		try:
			with open(self.Wordlist, "rb") as PasswordWordlist:
				self.Passwords = [Line.strip() for Line in PasswordWordlist if (Line.strip())]
		except Exception:
			self.Cmd.Clear(f"{sd.eBan}{bc.BC} Failed to open Password Wordlist: {bc.RC} {self.Wordlist}\n", True)
		
	def CrackPassword(self):
		if (self.Validator.NotEmpty(self.Passwords)):
			for Password in self.Passwords:
				if (self.Validator.NotEmpty(self.FoundPassword)):
					break

				PasswordString = Password.decode("utf-8", errors="ignore")

				self.Console.Raw(f"[{bc.GC}{self.Tries}{bc.BC}] Trying Password:{bc.GC} {PasswordString}")

				try:
					with zipfile.ZipFile(self.ZipFile, "r") as ZF:						
						os.makedirs(self.ExtractToPath, exist_ok=True)

						for Member in ZF.infolist():
							if (Member.is_dir()):
								continue # skip directories

							OriginalName = Member.filename
							FileName = os.path.basename(OriginalName)

							if (not FileName):
								continue # skip if no valid filename

							TargetPath = os.path.join(self.ExtractToPath, FileName)

							with ZF.open(Member, pwd=Password) as Source, open(TargetPath, "wb") as Target:
								Target.write(Source.read())

							FileSize = round(os.path.getsize(TargetPath) / 1024, 2)
							FileInfo = f"{FileName}:#:{FileSize} KB"
							self.ResponseData.append(FileInfo)

						self.FoundPassword = PasswordString

				except RuntimeError as e:
					if ("Bad password" in str(e)):
						self.Tries += 1

						continue

	def DisplayResults(self):
		self.Cmd.Clear()
		self.Console.Raw(f"Password Wordlist:{bc.GC} {self.Wordlist}", False)
		self.Console.Raw(f"Zip File:{bc.GC} {self.ZipFile}")
		self.Console.Success(f"Password Found:{bc.GC} {self.FoundPassword}")
		self.Console.Raw(f"Extracted Contents:")

		FileCount = 1

		for Dat in self.ResponseData:
			Dat = str(Dat)

			File = Dat.split(':#:')[0]
			Size = Dat.split(':#:')[1]
			
			self.Console.Raw(f"[{bc.GC}File {FileCount}{bc.BC}]:{bc.GC} {File}", False, True)
			self.Console.Raw(f"[{bc.GC}Size{bc.BC}]:{bc.GC} {Size}", True, True)

			FileCount += 1
		
		self.Console.Success(f"Extraction Complete")

		Initiate()

	def Rip(self):
		self.SetWordlist()
		self.SetZipFile()
		self.SetZipFileDirectory()
		self.SetPasswords()
		self.CrackPassword()
		self.DisplayResults()		

if (__name__ == "__main__"):
	def Initiate():
		try:
			ZipRip().Rip()
		except KeyboardInterrupt:
			quit()

	Command().Clear()
	Initiate()

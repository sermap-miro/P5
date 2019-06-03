from string import*
from os import system
import sys
import re
import os
class Maker_U:
	file1 = "liste_python.txt"
	file2 = "Uploader_Project_P5.sh"
	wc = "r"
	head = "#!/bin/bash\n"
	login="sermap"
	passw="sermapP5"
	ip="192.168.4.1"
	port="21"
	Curl_opt="-3 --ftp-ssl"
	w_folder=".."
	mpy_folder="../MPYFOLDER"
	prgm_f="../prgm"
	
	
				
	def __init__(self):
		pass
		
	def first_step(self):
		system("cd ../MPYFILES && ls *.mpy > ../maker_Uploader/{} && cd ../maker_Uploader/".format(self.file1))
		liste_py = open(self.file1,"r")
		
		try:
			texte = liste_py.read()
			filepy = texte.split('\n')
			filepy.remove("")
			print(len(filepy))
			liste_py.close()
			
		except IOError:
			print("Impossible d'ouvrir le fichier {}.".format(self.file1))
			sys.exit(-1)
		self.f_Up = open(self.file2,"w")
		
		try:
			self.f_Up.write(self.head)
			self.f_Up.write("#\t\t\tListe des fichiers mpy.\n")
			for i in filepy:
				self.f_Up.write('echo "Chargement du fichier {0}" \n'.format(i))
				line_in = "curl {0} -T {1}/{2} ftp://{3}:{4}@{5}:{6}/flash/\n".format(self.Curl_opt,self.mpy_folder,i,self.login,self.passw,self.ip,self.port)
				self.f_Up.write(line_in)
			self.f_Up.write("\n")
			self.f_Up.close()	
		except IOError:
			print("Impossible d'ouvrir le fichier {}.".format(self.file2))
			sys.exit(-1)
			
	def repf(self,f_ext=""):
		
		if ((f_ext == "htm" )|(f_ext == "txt") |( f_ext =="ico")):
			system("cd .. && ls *.{0} > maker_Uploader/{0}.txt && cd maker_Uploader/".format(f_ext))
			file_t ="{}.txt".format(f_ext)
			
			try:
				liste_py = open(file_t,"r")	
				texte = liste_py.read()
				filepy = texte.split('\n')
				filepy.remove("")
				print(len(filepy))
				liste_py.close()
		
			except IOError:
				print("Impossible d'ouvrir le fichier {}.".format(self.file1))
				sys.exit(-1)
				
			try:
				self.f_Up = open(self.file2,"a")
				self.f_Up.write("#\t\t\tListe des fichiers {}.\n".format(f_ext))
				for i in filepy:
					self.f_Up.write('echo "Chargement du fichier {0}" \n'.format(i))
					word = "curl {0} -T {1}/{2} ftp://{3}:{4}@{5}:{6}/flash/\n".format(self.Curl_opt,self.w_folder,i,self.login,self.passw,self.ip,self.port)
					self.f_Up.write(word)
				self.f_Up.write("\n")
				self.f_Up.close()
				
			except IOError:
				print("Impossible d'ouvrir le fichier {}.".format(self.file2))
				sys.exit(-1)
				
		elif (f_ext == "main.py"):
		
			try:
				self.f_Up = open (self.file2, "a")
				self.f_Up.write("#\t\t\t Le {}.\n".format(f_ext))
				self.f_Up.write('echo "Chargement du fichier main.py" \n')
				self.f_Up.write("curl {0} -T {1}/{6} ftp://{2}:{3}@{4}:{5}/flash/\n\n".format(self.Curl_opt,self.w_folder,self.login,self.passw,self.ip,self.port,f_ext))
			
			except IOError:
				print("Impossible d'ouvrir le fichier {}.".format(self.file2))
		elif (f_ext == "prgm"):
			system("cd ../{0} && ls *.txt > ../maker_Uploader/{0}.txt && cd ../maker_Uploader/".format(f_ext))
			# system("cd ../MPYFILES && ls *.mpy > ../maker_Uploader/{} && cd ../maker_Uploader/".format(self.file1))
			file_t ="{}.txt".format(f_ext)
			liste_py = open(file_t,"r")
			try:	
				texte = liste_py.read()
				filepy = texte.split('\n')
				filepy.remove("")
				print(len(filepy))
				liste_py.close()
		
			except IOError:
				print("Impossible d'ouvrir le fichier {}.".format(self.file1))
				sys.exit(-1)
		
			try:
				self.f_Up = open(self.file2,"a")
				self.f_Up.write("#\t\t\tListe des fichiers {}.\n".format(f_ext))
				for i in filepy:
					self.f_Up.write('echo "Chargement du fichier {0}" \n'.format(i))
					word = "curl {0} -T {1}/{2} ftp://{3}:{4}@{5}:{6}/flash/prgm/\n".format(self.Curl_opt,self.prgm_f,i,self.login,self.passw,self.ip,self.port)
					self.f_Up.write(word)
				self.f_Up.write("\n")
				self.f_Up.close()
				
			except IOError:
				print("Impossible d'ouvrir le fichier {}.".format(self.file2))
				sys.exit(-1)
		elif f_ext == "":
			print("Paramètre vide")
		else:
			print("Paramètre non reconnnu")

mak = Maker_U()
mak.first_step()
mak.repf("htm")
mak.repf("ico")
mak.repf("main.py")
mak.repf("txt")
mak.repf("prgm")


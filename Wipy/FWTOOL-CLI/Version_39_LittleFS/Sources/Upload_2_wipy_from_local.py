import ftplib
from ftplib import FTP
import time
ERREUR = 0
LISTE_ERREUR = ''
LOGIN="sermap"
PASS="sermapP5"
IP= "192.168.4.1"
PORT="21"
ftp_obj = FTP()
Temps_Pause_Inter_Send = 0.1
ftp_obj.connect(IP, 21)
ftp_obj.login(user = LOGIN, passwd = PASS)
serverdirectorypath='/flash'
ftp_obj.cwd(serverdirectorypath)
print('Listing des fichiers présent dans le répertoire /flash du wipy avant la mise à jour')
ftp_obj.retrlines('LIST') # list directory contents
print("Debut de l'update...")
LISTE_FICHIER = ['main.py', 'mirobot2.py', 'pion.py', 'config.py', 'es.py', 'planning.py', 'commande.py', 'main.html', 'AiCwebserver.py', 'wifi.py']
if(False):
	LISTE_FICHIER.append('planning.txt')

if(True):
	for _ in LISTE_FICHIER:

		resultat_fonction = ftp_obj.storbinary('STOR {}'.format(_), open('{}'.format(_), 'rb'))
		if resultat_fonction != '226 ':
			ERREUR += 1
			print('Erreur lors du transfert de {}'.format(_))
		else:
			print('{} transfer pass'.format(_))
		time.sleep(Temps_Pause_Inter_Send)
print('Listing des fichiers présent dans le répertoire /flash du wipy après la mise à jour')
ftp_obj.retrlines('LIST')

if(False):
	serverdirectorypath='/flash/prgm'
	ftp_obj.cwd(serverdirectorypath)

	print('Listing des fichiers présent dans le répertoire /flash/prgm du wipy avant la mise à jour')
	ftp_obj.retrlines('LIST') # list directory contents

	for _ in ('DVT.txt', 'MultiTas.txt', 'Pailleux.txt', 'Retour.txt', 'Standard.txt'):
		resultat_fonction = ftp_obj.storbinary('STOR {}'.format(_), open('prgm/{}'.format(_), 'rb'))
		if resultat_fonction != '226 ':
			ERREUR += 1
			print('Erreur lors du transfert de {}'.format(_))
		time.sleep(Temps_Pause_Inter_Send)

print('Listing des fichiers présent dans le répertoire /flash du wipy après la mise à jour')
ftp_obj.retrlines('LIST') # list directory contents
print("Fin de l'update")

if ERREUR > 0:
	print('!!! {0} erreur{1} détectée{1} !!!'.format(ERREUR, 's' if ERREUR > 1 else ''))
else:
	print('Aucune erreur détectée')
print('Appuyez sur la touche "Enter" pour fermer la fenêtre')
while(True):
	try:
		key = input("")
		if (len(key) >= 0):
			break
	except:
		pass
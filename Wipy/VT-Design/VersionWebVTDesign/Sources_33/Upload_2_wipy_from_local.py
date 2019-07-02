
import ftplib
from ftplib import FTP
import time
#
#!/bin/bash
#./Upload_2_wipy_from_local.sh 1 . 1
#./Upload_2_wipy_from_local.sh 0 . 0
# Premier Argument: Upload (1 = oui, 0 = non) des programmes préenregistré et d'un planning vierge
# Second Argument: Répertoire de travail (. = répertoire courant)
# Troisième Argument: Mot de passe utilisé pour la mise à jour: 1 lorsque la carte est vierge, 0 lorsque la carte à déjà été configurer
#curl -3 --ftp-ssl ftp://sermap:sermapP5@192.168.4.11/flash/wifi_name.txt -o wifi_name.txt

#./Upload_2_wipy_from_local.sh 00005 1 . 1
#./Upload_2_wipy_from_local.sh 00005 0 . 0
# Premier Argument: Nom du point d'acces Réseaux
# Second Argument: Upload (1 = oui, 0 = non) des programmes préenregistré
# Troisième Argument: Répertoire de travail (. = répertoire courant)
# Quatrième Argument: Mot de passe utilisé pour la mise à jour: 1 lorsque la carte est vierge, 0 lorsque la carte à déjà été configurer


#  curl -3 --ftp-ssl -T mirobot2.py ftp://sermap:sermapP5@192.168.4.1:21/flash/

ERREUR = 0
LISTE_ERREUR = ''

#if (( "$3" == "1" )) ; then
#echo -e "Mot de passe micro/python"

#LOGIN=micro
#PASS=python

#else
#echo -e "Mot de passe sermap/P5"

LOGIN="sermap"
PASS="sermapP5"

#fi

#LOGIN=sermap
#PASS=sermapP5

#LOGIN=micro
#PASS=python

IP= "192.168.4.1"
PORT="21"

ftp_obj = FTP()
 
Temps_Pause_Inter_Send = 0.1


ftp_obj.connect(IP, 21)
#ftp_obj.connect(IP, PORT)
ftp_obj.login(user = LOGIN, passwd = PASS)


serverdirectorypath='/flash'
ftp_obj.cwd(serverdirectorypath)

print('Listing des fichiers présent dans le répertoire /flash du wipy avant la mise à jour')
ftp_obj.retrlines('LIST') # list directory contents

#==>FTP.delete(filename)
#1
	
#ftp_obj.delete(serverfilepath)

#This use to retrieve a file in form of binary transfer mode.
#Like:
#1
	
#ftp.retrbinary('RETR %s'%serverfilepath, open(localfilepath, 'wb').write)


#WORKING_FOLDER=/home/sam/Lab/Programmes/Electronique/Pyboard/P4

#WORKING_FOLDER=.
#WORKING_FOLDER=$2

#CURL_OPTION="-3 --ftp-ssl"
#CURL_OPTION="-3 -v --ftp-ssl"

#echo -e "Debut de l'update..."
print("Debut de l'update...")
#if (( "1" == "0" )) ; then
#connexion_ftp = ftplib(IP, LOGIN, PASS)
#This use to upload the data over the server.
#1
	
#ftp_obj.storbinary('STOR %s'%serverfilepath, = open(localfilepath, 'rb'))

#for _ in ('main.py', 'mirobot2.py', 'P4.py', 'pion.py', 'config.py', 'es.py' ,'planning.py' ,'commande.py' ,'AiCmirobot.htm' ,'AiCmirobot_p.htm' ,'AiCwebserver.py' ,'wifi.py'):


LISTE_FICHIER = ['main.py', 'mirobot2.py', 'pion.py', 'config.py', 'es.py', 'planning.py', 'commande.py', 'AiCmirobot.htm', 'AiCmirobot_p.htm', 'AiCmirobot_header.htm', 'AiCmirobot_planning.htm', 'AiCmirobot_planning_header.htm', 'AiCmirobot_info.htm', 'AiCmirobot_wifi.htm', 'AiCmirobot_etat_header.htm', 'AiCmirobot_conf_header.htm', 'AiCmirobot_clock_header.htm', 'AiCmirobot_menu_principal_begin.htm', 'AiCmirobot_menu_principal_end.htm', 'AiCwebserver.py', 'wifi.py']

#LISTE_FICHIER = ['AiCmirobot.htm', 'AiCmirobot_clock_header.htm', 'AiCmirobot_conf_header.htm', 'AiCmirobot_etat_header.htm', 'AiCmirobot_header.htm', 'AiCmirobot_info.htm', 'AiCmirobot_menu_principal_begin.htm', 'AiCmirobot_menu_principal_end.htm', 'AiCmirobot_p.htm', 'AiCmirobot_planning.htm', 'AiCmirobot_planning_header.htm', 'AiCmirobot_wifi.htm', 'AiCwebserver.py', 'commande.py', 'config.py', 'es.py', 'main.py', 'mirobot2.py', 'pion.py', 'planning.py', 'planning.txt', 'wifi.py']

if(False):
 LISTE_FICHIER.append('planning.txt')


if(True):
 for _ in LISTE_FICHIER:
 #for _ in ('main.py', 'mirobot2.py', 'pion.py', 'config.py', 'es.py', 'planning.py', 'commande.py', 'AiCmirobot.htm', 'AiCmirobot_p.htm', 'AiCmirobot_header.htm', 'AiCmirobot_planning.htm', 'AiCmirobot_planning_header.htm', 'AiCmirobot_info.htm', 'AiCmirobot_wifi.htm', 'AiCmirobot_etat_header.htm', 'AiCmirobot_conf_header.htm', 'AiCmirobot_clock_header.htm', 'AiCmirobot_menu_principal_begin.htm', 'AiCmirobot_menu_principal_end.htm', 'AiCwebserver.py', 'wifi.py', 'planning.txt'):
  resultat_fonction = ftp_obj.storbinary('STOR {}'.format(_), open('{}'.format(_), 'rb'))
  if resultat_fonction != '226 ':
   ERREUR += 1
   print('Erreur lors du transfert de {}'.format(_))
  else:
   print('{} transfer pass'.format(_))
  time.sleep(Temps_Pause_Inter_Send)


print('Listing des fichiers présent dans le répertoire /flash du wipy après la mise à jour')
ftp_obj.retrlines('LIST') # list directory contents
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/main.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/



#sleep 0.3
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/mirobot2.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

#sleep 0.3
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/P4.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

#sleep 0.3
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/pion.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

#sleep 0.3
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/config.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

#sleep 0.3
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/es.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/


#sleep 0.3
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/planning.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

#sleep 0.3
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/commande.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

#sleep 0.3
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/AiCmirobot.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#sleep 0.3
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/AiCmirobot_p.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

#sleep 0.3
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/AiCwebserver.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/



#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/wifi.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/



#==>FTP.mkd(pathname)
#To create a new directory on given path (pathname).
#1	
#ftp_obj.mkd(serverdirectorypath)

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

#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/prgm/DVT.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/ --ftp-create-dirs
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/prgm/MultiTas.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/ --ftp-create-dirs
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/prgm/Pailleux.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/ --ftp-create-dirs
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/prgm/Retour.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/ --ftp-create-dirs
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/prgm/Standard.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/ --ftp-create-dirs






print("Fin de l'update")

if ERREUR > 0:
 print('!!! {0} erreur{1} détectée{1} !!!'.format(ERREUR, 's' if ERREUR > 1 else ''))
else:
 print('Aucune erreur détectée')


print('Appuyez sur la touche "Enter" pour fermer la fenêtre')
while(True):
 try:
  #key = input("Appuyez sur une touche pour fermer la fenêtre")
  key = input("")
  if (len(key) >= 0):
   break
 except:
  pass




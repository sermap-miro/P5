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


if (( "$3" == "1" )) ; then
echo -e "Mot de passe micro/python"

LOGIN=micro
PASS=python

else
echo -e "Mot de passe sermap/P5"

LOGIN=sermap
PASS=sermapP5

fi

#LOGIN=sermap
#PASS=sermapP5

#LOGIN=micro
#PASS=python

IP=192.168.4.1
PORT=21

CURL_OPTION="-3 --ftp-ssl"
#CURL_OPTION="-3 -v --ftp-ssl"

#WORKING_FOLDER=/home/sam/Lab/Programmes/Electronique/Pyboard/P4

#
WORKING_FOLDER=.
WORKING_FOLDER=$2


echo -e "Debut de l'update..."

#if (( "1" == "0" )) ; then


#sleep 0.3
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/AiCwebserver.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

until curl ${CURL_OPTION} -T ${WORKING_FOLDER}/AiCwebserver_CMD.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/; do
  echo Tansfer disrupted, retrying in 10 seconds...
  #sleep 10
done

until curl ${CURL_OPTION} -T ${WORKING_FOLDER}/AiCwebserver.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/; do
  echo Tansfer disrupted, retrying in 10 seconds...
  #sleep 10
done
#echo "abc" | cat wifi_pre.txt - wifi_post.txt > wifi.txt

#On enregistre le numéro de l'identification dans un fichier (dans le repertoire /tmp)
#echo $1 > /tmp/MIRID.txt

#head -c -1 -q ${WORKING_FOLDER}/wifi_pre.txt /tmp/MIRID.txt ${WORKING_FOLDER}/wifi_post.txt > ${WORKING_FOLDER}/wifi.py



echo -e "Fin de l'update"


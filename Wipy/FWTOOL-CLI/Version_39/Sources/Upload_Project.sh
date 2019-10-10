#!/bin/bash

LOGIN=micro
PASS=python
IP=192.168.4.1
PORT=21
CURL_OPTION="-3 --ftp-ssl"
CURRENT_FOLDER=.

#Création des dossiers
echo Création du dossier assets
curl ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/  --ftp-create-dirs
echo Création du dossier prgm
curl ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/ --ftp-create-dirs
echo Création du dossier js
curl ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/js/ --ftp-create-dirs
echo Création du dossier json
curl ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/json/ --ftp-create-dirs
echo Création du dossier css
curl ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/css/ --ftp-create-dirs
echo Création du dossier img
curl ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/img/ --ftp-create-dirs

echo 'PYTHON FILES=12(11 mpy + 1 py)'
echo AiCwebserver_CMD.mpy
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCwebserver_CMD.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
echo AiCwebserver.mpy
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCwebserver.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
echo commande.mpy
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/commande.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
echo config.mpy
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/config.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
echo es.mpy
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/es.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
echo main_metlahome.mpy
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/main_metlahome.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
echo main.py
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/main.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
echo mirobot2.mpy
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/mirobot2.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
echo P4.mpy
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/P4.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
echo pion.mpy
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/pion.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
echo planning.mpy
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/planning.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
echo wifi.mpy
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/wifi.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

echo HTML FILE
echo index.html
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/index.html ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

#FAVICON.ICO
echo favicon.ico
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/favicon.ico ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

#ASSETS
echo 'CSS FILES (2 files)'
echo bootstrap.min.css
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/css/bootstrap.min.css ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/css/
echo miro.css
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/css/miro.css ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/css/


#LOGO ET IMAGES
echo l_white.png
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/img/l_white.png ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/img

echo done.png
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/img/done.png ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/img/
echo clear.png
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/img/clear.png ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/img/

echo 'JAVASCRIPT FILES (3 files)'
echo bootstrap.bundle.min.js
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/js/bootstrap.bundle.min.js ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/js/
echo jquery-3.3.1.min.js
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/js/jquery-3.3.1.min.js ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/js/
echo main.min.js
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/js/main.min.js ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/js/

#PLANNING.TXT
echo planning.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/planning.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/

#PRGM 
echo 1.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/1.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo 2.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/2.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo 3.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/3.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo 4.txt 
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/4.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo 5.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/5.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo 6.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/6.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo 7.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/7.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo 8.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/8.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo 9.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/9.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo DVT.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/DVT.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo MultiTas.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/MultiTas.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo Pailleux.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/Pailleux.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo Retour.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/Retour.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
echo Standard.txt
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/Standard.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
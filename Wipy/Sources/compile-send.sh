#!/bin/bash

rm -f MPYFILES/*.mpy

mpy-cross AiCwebserver_CMD.py
mv -f AiCwebserver_CMD.mpy ./MPYFILES
mpy-cross AiCwebserver.py 
mv -f AiCwebserver.mpy ./MPYFILES
mpy-cross commande.py 
mv -f commande.mpy ./MPYFILES
mpy-cross config.py 
mv -f config.mpy  ./MPYFILES
mpy-cross es.py 
mv -f es.mpy ./MPYFILES
mpy-cross main_metlahome.py 
mv -f main_metlahome.mpy ./MPYFILES
mpy-cross mirobot2.py 
mv -f mirobot2.mpy ./MPYFILES
mpy-cross P4.py 
mv -f P4.mpy ./MPYFILES
mpy-cross pion.py 
mv -f pion.mpy ./MPYFILES
mpy-cross wifi.py 
mv -f wifi.mpy ./MPYFILES

./COMPILE_PY
LOGIN=sermap
PASS=sermapP5
IP=192.168.4.1
PORT=21
CURL_OPTION="-3 --ftp-ssl"
MPY_FOLDER=MPYFILES
CURRENT_FOLDER=.
#MPY FILES
curl ${CURL_OPTION} -T ${MPY_FOLDER}/AiCwebserver_CMD.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${MPY_FOLDER}/AiCwebserver.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${MPY_FOLDER}/commande.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${MPY_FOLDER}/config.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${MPY_FOLDER}/es.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${MPY_FOLDER}/main_metlahome.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/main.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${MPY_FOLDER}/mirobot2.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${MPY_FOLDER}/P4.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${MPY_FOLDER}/pion.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${MPY_FOLDER}/wifi.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#HTM FILES
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_calibration.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_clock_header.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_conf_header.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_edit_header.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_etat_header.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_header.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_info.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_menu_principal_begin.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_menu_principal_end.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_p.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_planning_header.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/AiCmirobot_planning.htm ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#FAVICON.ICO
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/favicon.ico ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#ASSETS
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/css/bootstrap.min.css ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/css/miro.css ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/css/miro.responsive.css ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/img/logo.png ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/js/bootstrap.bundle.min.js ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/js/jquery-3.3.1.min.js ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/js/main.min.js ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/


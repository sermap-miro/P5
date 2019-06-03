#!/bin/bash
./COMPILE_PY
LOGIN=micro
PASS=python
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
curl ${CURL_OPTION} -T ${MPY_FOLDER}/planning.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
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
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/css/bootstrap.min.css ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/css/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/css/miro.css ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/css/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/css/miro.responsive.css ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/css/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/img/logo.png ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/img/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/js/bootstrap.bundle.min.js ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/js/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/js/jquery-3.3.1.min.js ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/js/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/assets/js/main.min.js ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/assets/js/
#PLANNING.TXT
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/planning.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#PRGM 
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/1.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/DVT.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/MultiTas.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/Pailleux.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/Retour.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/
curl ${CURL_OPTION} -T ${CURRENT_FOLDER}/prgm/Standard.txt ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/prgm/

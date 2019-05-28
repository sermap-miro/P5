#!/bin/bash


#ssh pwin "curl -3 -v --ftp-ssl -T /home/sam/Lab/Electronique/Pyboard/P4/prgm/DVT.txt ftp://micro:python@192.168.4.1:21/flash/prgm/ --ftp-create-dirs"

#scp -r main.py mirobot.py plinux:"'/home/sam/Lab/Electronique/Pyboard/Mirobot 3.0/'"

./COMPILE_PY


#ssh plinux "curl -3 -v --ftp-ssl -T '/home/sam/Lab/Electronique/Pyboard/Mirobot 3.0/mirobot.py' ftp://micro:python@192.168.4.1:21/flash/ --ftp-create-dirs"
#sleep 0.3


#LOGIN=a
#PASS=a

#LOGIN=sermap
#PASS=sermapP5

#LOGIN=micro
#PASS=python

LOGIN=sermap
PASS=sermapP5


IP=192.168.4.1

PORT=21

CURL_OPTION="-3 --ftp-ssl"
#CURL_OPTION="-3 -v --ftp-ssl"

#WORKING_FOLDER=/home/sam/Lab/Programmes/Electronique/Pyboard/P4

#
WORKING_FOLDER=./MPY_FILES
#WORKING_FOLDER=$2



#sleep 0.3
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/AiCwebserver_CMD.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/AiCwebserver..mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/commande.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/config.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/es.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/main_metlahome.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T main.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/mirobot2.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/P4.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/pion.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/wifi.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/planning.mpy ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#sleep 0.3
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/circuit.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/clock.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/es.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/ihm.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/interception.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/lora.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/main.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/mirobot.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/
#curl ${CURL_OPTION} -T ${WORKING_FOLDER}/rfid.py ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/



#ssh plinux "rm /home/sam/Lab/Electronique/Pyboard/GPS/main.py; ln -s /home/sam/Lab/Electronique/Pyboard/GPS/main_pytrack.py /home/sam/Lab/Electronique/Pyboard/GPS/main.py" && ssh plinux "curl -3 -v --ftp-ssl -T /home/sam/Lab/Electronique/Pyboard/GPS/main.py ftp://micro:python@192.168.43.225:21/flash/"
#sleep 0.3

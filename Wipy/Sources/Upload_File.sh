LOGIN=sermap
PASS=sermapP5
IP=192.168.4.1
PORT=21
CURL_OPTION="-3 --ftp-ssl"
WORKING_FOLDER=.
echo -e "Debut de l'update..."
echo -e "Envoi du fichier: ${WORKING_FOLDER}/${1}"
echo -e "dans: /flash/${2}"
curl ${CURL_OPTION} -T ${WORKING_FOLDER}/${1} ftp://${LOGIN}:${PASS}@${IP}:${PORT}/flash/${2}
echo -e "Fin de l'update"
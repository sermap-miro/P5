#!/bin/bash
#			Liste des fichiers mpy.
echo "Chargement du fichier AiCwebserver_CMD.mpy" 
curl -3 --ftp-ssl -T ../MPYFILES/AiCwebserver_CMD.mpy ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier AiCwebserver.mpy" 
curl -3 --ftp-ssl -T ../MPYFILES/AiCwebserver.mpy ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier commande.mpy" 
curl -3 --ftp-ssl -T ../MPYFILES/commande.mpy ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier config.mpy" 
curl -3 --ftp-ssl -T ../MPYFILES/config.mpy ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier es.mpy" 
curl -3 --ftp-ssl -T ../MPYFILES/es.mpy ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier main_metlahome.mpy" 
curl -3 --ftp-ssl -T ../MPYFILES/main_metlahome.mpy ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier mirobot2.mpy" 
curl -3 --ftp-ssl -T ../MPYFILES/mirobot2.mpy ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier P4.mpy" 
curl -3 --ftp-ssl -T ../MPYFILES/P4.mpy ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier pion.mpy" 
curl -3 --ftp-ssl -T ../MPYFILES/pion.mpy ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier planning.mpy" 
curl -3 --ftp-ssl -T ../MPYFILES/planning.mpy ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier wifi.mpy" 
curl -3 --ftp-ssl -T ../MPYFILES/wifi.mpy ftp://micro:python@192.168.4.1:21/flash/

#			Liste des fichiers htm.
echo "Chargement du fichier calibration.htm" 
curl -3 --ftp-ssl -T ../calibration.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier clock.htm" 
curl -3 --ftp-ssl -T ../clock.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier configuration.htm" 
curl -3 --ftp-ssl -T ../configuration.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier edit.htm" 
curl -3 --ftp-ssl -T ../edit.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier footer.htm" 
curl -3 --ftp-ssl -T ../footer.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier header.htm" 
curl -3 --ftp-ssl -T ../header.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier header_mp.htm" 
curl -3 --ftp-ssl -T ../header_mp.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier head.htm" 
curl -3 --ftp-ssl -T ../head.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier info.htm" 
curl -3 --ftp-ssl -T ../info.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier manuel.htm" 
curl -3 --ftp-ssl -T ../manuel.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier menu_principal.htm" 
curl -3 --ftp-ssl -T ../menu_principal.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier planning.htm" 
curl -3 --ftp-ssl -T ../planning.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier programme.htm" 
curl -3 --ftp-ssl -T ../programme.htm ftp://micro:python@192.168.4.1:21/flash/
echo "Chargement du fichier wifi.htm" 
curl -3 --ftp-ssl -T ../wifi.htm ftp://micro:python@192.168.4.1:21/flash/

#			Liste des fichiers ico.
echo "Chargement du fichier favicon.ico" 
curl -3 --ftp-ssl -T ../favicon.ico ftp://micro:python@192.168.4.1:21/flash/

#			 Le main.py.
echo "Chargement du fichier main.py" 
curl -3 --ftp-ssl -T ../main.py ftp://micro:python@192.168.4.1:21/flash/

#			Liste des fichiers txt.
echo "Chargement du fichier planning.txt" 
curl -3 --ftp-ssl -T ../planning.txt ftp://micro:python@192.168.4.1:21/flash/

#			Liste des fichiers prgm.
echo "Chargement du fichier 1.txt" 
curl -3 --ftp-ssl -T ../prgm/1.txt ftp://micro:python@192.168.4.1:21/flash/prgm/
echo "Chargement du fichier DVT.txt" 
curl -3 --ftp-ssl -T ../prgm/DVT.txt ftp://micro:python@192.168.4.1:21/flash/prgm/
echo "Chargement du fichier MultiTas.txt" 
curl -3 --ftp-ssl -T ../prgm/MultiTas.txt ftp://micro:python@192.168.4.1:21/flash/prgm/
echo "Chargement du fichier Pailleux.txt" 
curl -3 --ftp-ssl -T ../prgm/Pailleux.txt ftp://micro:python@192.168.4.1:21/flash/prgm/
echo "Chargement du fichier Retour.txt" 
curl -3 --ftp-ssl -T ../prgm/Retour.txt ftp://micro:python@192.168.4.1:21/flash/prgm/
echo "Chargement du fichier Standard.txt" 
curl -3 --ftp-ssl -T ../prgm/Standard.txt ftp://micro:python@192.168.4.1:21/flash/prgm/

#			Liste des feuilles de style css.
echo "Chargement du fichier bootstrap.min.css" 
curl -3 --ftp-ssl -T ../assets/css/bootstrap.min.css ftp://micro:python@192.168.4.1:21/flash/assets/css/
echo "Chargement du fichier miro.css" 
curl -3 --ftp-ssl -T ../assets/css/miro.css ftp://micro:python@192.168.4.1:21/flash/assets/css/
echo "Chargement du fichier miro.responsive.css" 
curl -3 --ftp-ssl -T ../assets/css/miro.responsive.css ftp://micro:python@192.168.4.1:21/flash/assets/css/

#			Liste des js.
echo "Chargement du fichier bootstrap.bundle.min.js" 
curl -3 --ftp-ssl -T ../assets/js/bootstrap.bundle.min.js ftp://micro:python@192.168.4.1:21/flash/assets/js/
echo "Chargement du fichier jquery-3.3.1.min.js" 
curl -3 --ftp-ssl -T ../assets/js/jquery-3.3.1.min.js ftp://micro:python@192.168.4.1:21/flash/assets/js/
echo "Chargement du fichier main.min.js" 
curl -3 --ftp-ssl -T ../assets/js/main.min.js ftp://micro:python@192.168.4.1:21/flash/assets/js/

#			Liste des img.
echo "Chargement du fichier logo.png" 
curl -3 --ftp-ssl -T ../assets/img/logo.png ftp://micro:python@192.168.4.1:21/flash/assets/img/


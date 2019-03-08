#!/bin/bash
#curl "https://software.pycom.io/findupgrade?key=wipy.wipy%20with%20esp32&redirect=false&type=all"

#echo "Reset Complet du Wipy"
if [ -d IpeCMDlog/ ]; then
echo "Le Dossier IpeCMDlog existe"
else
mkdir IPECMDlog
fi

ipecmd -TPICD3 -M -Y -P18F4431 -F../../../PIC_18f4431/Moteur_P4/dist/default/production/Moteur_P4.production.hex
mv log.* IpeCMDlog/
mv MPLABXLog.xml* IpeCMDlog/
rm -rf IpeCMDlog

 
read -n1 -r -p "Reset Complet du Wipy ? Press space to continue..." key
#Reset Complet: 
pycom-fwtool-cli -v -p COM6 erase_all



#echo "Install du système du Wipy"
read -n1 -r -p "Install du système du Wipy? Press space to continue..." key
#Update
pycom-fwtool-cli --port COM6 --verbose  flash -t WiPy-1.18.1.r1.tar.gz



#Make Backup
#pycom-fwtool-cli --port /dev/ttyUSB0 --verbose  copy -p fs1

#echo "Installation du programme P5 pour le Wipy"
read -n1 -r -p "Installation du programme P5 pour le Wipy? Press space to continue..." key
#Restore
pycom-fwtool-cli --port COM6 --verbose copy -p fs1 -r -f Version_37.bin
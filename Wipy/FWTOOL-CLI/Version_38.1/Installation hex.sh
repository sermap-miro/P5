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
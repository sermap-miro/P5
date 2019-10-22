if [ -d IpeCMDlog/ ]; then	
echo "Le Dossier IpeCMDlog existe"
else
mkdir IPECMDlog
fi

ipecmd -TPICD3 -M -Y -P18F4431 -F ../../../../PIC_18f4431/Moteur_P4/dist/default/production/Moteur_P4.production.hex
mv log.* IpeCMDlog/
mv MPLABXLog.xml* IpeCMDlog/
rm -rf IpeCMDlog
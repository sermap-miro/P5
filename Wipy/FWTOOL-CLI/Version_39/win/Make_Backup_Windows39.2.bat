#!/bin/bash

echo "Reset Complet du Wipy"

read -n1 -r -p "Reset Complet du Wipy ? Press space to continue..." key 
pycom-fwtool-cli -v -p $1 erase_all

read -n1 -r -p "Install du système du Wipy? Press space to continue..." key
pycom-fwtool-cli --port $1 --verbose  flash -t ../bin/WiPy-1.18.1.r1.tar.gz

read -n1 -r -p "Installation du programme P5 pour le Wipy? Press space to continue..." key
pycom-fwtool-cli --port $1 --verbose copy -p fs1 -r -f ../bin/Version_39.2.bin
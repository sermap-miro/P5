#!/bin/bash
#curl "https://software.pycom.io/findupgrade?key=wipy.wipy%20with%20esp32&redirect=false&type=all"

#Reset Complet: 
pycom-fwtool-cli -v -p /dev/ttyUSB0 erase_all

#Update
pycom-fwtool-cli --port /dev/ttyUSB0 --verbose  flash -t WiPy-1.18.1.r1.tar.gz

#Make Backup
#pycom-fwtool-cli --port /dev/ttyUSB0 --verbose  copy -p fs1

#Restore
pycom-fwtool-cli --port /dev/ttyUSB0 --verbose copy -p fs1 -r -f Version_27.bin




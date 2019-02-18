# -*- coding: utf-8 -*-


import network
from network import WLAN

from es import ARRET_URGENCE, BUZZER

# def Wifi_Write(Nom):
#     # _Fichier_Wifi_Nom = open('/flash/wifi_name.txt', "w+")
#     # _Fichier_Wifi_Nom.write(Nom)
#     # _Fichier_Wifi_Nom.close()
#     with open('/flash/wifi_name.txt', "w+") as _Fichier_Wifi_Nom:
#         _Fichier_Wifi_Nom.write(Nom)
#
#
#
# # with open('/flash/wifi_name.txt', "w+") as _f: _f.write(Nom)
#
# def Wifi_Delete():
#     import os
#     os.remove('/flash/wifi_name.txt')

#from mirobot2 import m

def Wifi_Init(_Nom_Wifi='P5'):
    # pycom.nvs_set('SID', int(self.PLATINE_TEMPS_100ms))
    # Memory_Value = pycom.nvs_get('SID')
    # if Memory_Value is not None:
    #     _Nom_Wifi = ' - ' + Memory_Value
    # try:
    #     _Fichier_Wifi_Nom = open('/flash/wifi_name.txt', "r")
    #     _Nom_Wifi = 'P5 - ' + _Fichier_Wifi_Nom.read()
    # except:
    #     _Nom_Wifi = 'P5'
    server = network.Server()
    server.deinit() # disable the server
    server.init(login=('sermap', 'sermapP5'), timeout=16000)
    #if True:
    #if ARRET_URGENCE() == 1: # il y a pas de metal en face du capteur
    if True:
        wlan = WLAN()
        #wlan.init(mode=WLAN.AP, ssid='P5 - 00010', auth=None, channel=7, antenna=WLAN.INT_ANT)
        wlan.init(mode=WLAN.AP, ssid=_Nom_Wifi, auth=None, channel=7, antenna=WLAN.INT_ANT)

        #wlan.ifconfig(id=1, config=('192.168.0.1', '255.255.255.0', '192.168.0.1', '8.8.8.8'))

# -*- coding: utf-8 -*-


import network
from network import WLAN, Server

from es import ARRET_URGENCE, BUZZER

from mirobot2 import m

from time import sleep

wlan = WLAN()

Wifi_Lock = 1
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


def Wipy_Server_Init():
    server = Server()
    server.deinit() # disable the server
    server.init(login=('sermap', 'sermapP5'), timeout=16000)





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
    # server = network.Server()
    # server.deinit() # disable the server
    # server.init(login=('sermap', 'sermapP5'), timeout=16000)
    #if True:
    #if ARRET_URGENCE() == 1: # il y a pas de metal en face du capteur
    if True:
        #wlan = WLAN()
        #wlan.init(mode=WLAN.AP, ssid='P5 - 00010', auth=None, channel=7, antenna=WLAN.INT_ANT)
        wlan.init(mode=WLAN.AP, ssid=_Nom_Wifi, auth=None, channel=7, antenna=WLAN.INT_ANT)
        #wlan.init(mode=WLAN.AP, ssid=m.wifi_name , auth=None, channel=7, antenna=WLAN.INT_ANT)
        #wlan.init(mode=WLAN.AP, ssid='wipy-wlan', auth=(WLAN.WPA2,'www.wipy.io'), channel=7, antenna=WLAN.INT_ANT)
        #wlan.init(mode=WLAN.AP, ssid='wipy-wlan', auth=(WLAN.WPA2,'www.wipy.io'), channel=7, antenna=WLAN.INT_ANT)
        #wlan.ifconfig(id=1, config=('192.168.0.1', '255.255.255.0', '192.168.0.1', '8.8.8.8'))


def Wifi_Perso():
    if ARRET_URGENCE() == 1: # il y a pas de metal en face du capteur (capot ouvert)
        Wifi_Local()
    else:
        print("Wifi Usine")
        import _thread
        wlan.init(mode=WLAN.AP, ssid='P5', auth=None, channel=7, antenna=WLAN.INT_ANT)
        _thread.start_new_thread(Wifi_Local_Delayed, ())

def Wifi_Local_Delayed():
    global Wifi_Lock
    from time import sleep
    #sleep(60)
    sleep(75)#une minute après le démarrage du site web (qui nécessite un peu moins de 20 s)
    #print('')
    if Wifi_Lock==1:
        Wifi_Local()

def Wifi_UnLock(Lock=0):
    global Wifi_Lock
    Wifi_Lock = Lock

def Wifi_Local():
    print("Wifi Access Point")
    try:
        m.wifi_nom = ''
        wifi_channel = 7
        # _Fichier_Wifi_Nom = open('/flash/wifi_name.txt', "r")
        # wifi_nom = _Fichier_Wifi_Nom.read()
        # _Fichier_Wifi_Nom.close()

        try:
            with open('/flash/wifi_channel.txt', "r") as _Fichier_Wifi_Channel:
                wifi_channel = _Fichier_Wifi_Channel.read()
            wifi_channel = int(wifi_channel)
        except:
            wifi_channel = 7


        with open('/flash/wifi_name.txt', "r") as _Fichier_Wifi_Nom:
            wifi_nom = _Fichier_Wifi_Nom.read()

        if len(wifi_nom)>0:
            try:
                # _Fichier_Wifi_Password = open('/flash/wifi_password.txt', "r")
                # wifi_password = _Fichier_Wifi_Password.read()
                # _Fichier_Wifi_Password.close()
                with open('/flash/wifi_password.txt', "r") as _Fichier_Wifi_Password:
                    wifi_password = _Fichier_Wifi_Password.read()
            except:
                wifi_password = ''
            m.wifi_nom = wifi_nom
            m.wifi_name = 'P5 - ' + wifi_nom
            m.wifi_password = wifi_password
            m.wifi_channel = wifi_channel
            if len(m.wifi_password)>0:
                wlan.init(mode=WLAN.AP, ssid=m.wifi_name, auth=(WLAN.WPA2,m.wifi_password), channel=wifi_channel, antenna=WLAN.INT_ANT)
            else:
                #wlan.init(mode=WLAN.AP, ssid=m.wifi_name, auth=None, channel=7, antenna=WLAN.INT_ANT)
                raise MonException("Mot de passe vide")
        else:
            m.wifi_name = 'P5'
            m.wifi_nom = ''
            #m.wifi_channel = 7
            raise MonException("Valeur du SSID vide")
            #m.wifi_name = 'P5'
    except:
        #m.wifi_name = 'P5'
        #m.wifi_nom = ''
        wlan.init(mode=WLAN.AP, ssid=m.wifi_name, auth=None, channel=wifi_channel, antenna=WLAN.INT_ANT)

    # finally:
    #     if m.wifi_name == 'P5':
    #         wlan.init(mode=WLAN.AP, ssid=m.wifi_name, auth=None, channel=7, antenna=WLAN.INT_ANT)
    #     else:
    #         wlan.init(mode=WLAN.AP, ssid=m.wifi_name, auth=(WLAN.WPA2,m.wifi_password), channel=7, antenna=WLAN.INT_ANT)
    #         #wlan.connect(ssid=_ssid, auth=(WLAN.WPA2, _password))


#from network import WLAN
#Wifi_Connect('Mirobot 3.0 - Marronniers', '12345678')
#_ssid = 'Mirobot 3.0 - Marronniers'
#_password = '12345678'
def Wifi_Connect(_ssid, _password):
    wlan = WLAN(mode=WLAN.STA)
    Liste_Station_Wifi = wlan.scan()
    for Station_Wifi in Liste_Station_Wifi:
        if _ssid in Station_Wifi:
            m.affiche('SSID trouvé dans les Stations disponible')
            #wlan.connect(mode=WLAN.STA, ssid=_ssid, auth=(WLAN.WPA2,_password), channel=7, antenna=WLAN.INT_ANT)
            wlan.connect(ssid=_ssid, auth=(WLAN.WPA2, _password))
            sleep(10) # on donne 4 secondes au wipy pour se connecter
            m.affiche('Connexion réussi? = {}'.format(wlan.isconnected()))
    if wlan.isconnected() == False:
        Wifi_Local()

#wlan.ifconfig()

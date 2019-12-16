import network
from network import WLAN, Server
from es import ARRET_URGENCE, BUZZER
from mirobot2 import m
from time import sleep
wlan = WLAN()
Wifi_Lock = 1
def Wipy_Server_Init():
    server = Server()
    server.deinit() # disable the server
    server.init(login=('sermap', 'sermapP5'), timeout=16000)

def Wifi_Init(_Nom_Wifi='P5'):
        wlan.init(mode=WLAN.AP, ssid=_Nom_Wifi, auth=None, channel=7, antenna=WLAN.EXT_ANT)

def Wifi_Perso():
    #wlan.ifconfig(id=1,config=("192.168.4.1","255.255.255.252","192.168.4.1","8.8.8.8")) # AP
    #print(wlan.ifconfig(id=0)) # STA
    #print(wlan.ifconfig(id=1))# AP
    if ARRET_URGENCE() == 1: # Si arret urgence est allumé
        Wifi_Local()
    else:
        print("Wifi Usine")
        import _thread
        wlan.init(mode=WLAN.AP, ssid='P5', auth=None, channel=7, antenna=WLAN.EXT_ANT)
        _thread.start_new_thread(Wifi_Local_Delayed, ())

def Wifi_Local_Delayed():
    global Wifi_Lock
    from time import sleep
    sleep(75)#une minute après le démarrage du site web (qui nécessite un peu moins de 20 s)
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
                with open('/flash/wifi_password.txt', "r") as _Fichier_Wifi_Password:
                    wifi_password = _Fichier_Wifi_Password.read()
            except:
                wifi_password = ''
            m.wifi_nom = wifi_nom
            m.wifi_name = 'P5 - ' + wifi_nom
            m.wifi_password = wifi_password
            m.wifi_channel = wifi_channel
            if len(m.wifi_password)>0:
                wlan.init(mode=WLAN.AP, ssid=m.wifi_name, auth=(WLAN.WPA2,m.wifi_password), channel=wifi_channel, antenna=WLAN.EXT_ANT)
            else:
                raise MonException("Mot de passe vide")
        else:
            m.wifi_name = 'P5'
            m.wifi_nom = ''
            raise MonException("Valeur du SSID vide")
    except:
        wlan.init(mode=WLAN.AP, ssid=m.wifi_name, auth=None, channel=wifi_channel, antenna=WLAN.EXT_ANT)

def Wifi_Connect(_ssid, _password):
    wlan = WLAN(mode=WLAN.STA)
    Liste_Station_Wifi = wlan.scan()
    for Station_Wifi in Liste_Station_Wifi:
        if _ssid in Station_Wifi:
            m.affiche('SSID trouvé dans les Stations disponible')
            wlan.ssid(_ssid)
            wlan.auth(_password)
            sleep(10) # on donne 4 secondes au wipy pour se connecter
            m.affiche('Connexion réussi? = {}'.format(wlan.isconnected()))
    if wlan.isconnected() == False:
        Wifi_Local()
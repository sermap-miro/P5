# -*- coding: utf-8 -*-


import network
from network import WLAN

from es import ARRET_URGENCE, BUZZER

def Wifi_Init():
    if True:
    #if ARRET_URGENCE() == 1: # il y a pas de metal en face du capteur
        server = network.Server()
        server.deinit() # disable the server
        # # enable the server again with new settings
        # server.init(login=('sermap', 'sermap25'), timeout=16000)
        server.init(login=('sermap', 'sermapP5'), timeout=16000)

        wlan = WLAN()
        #wlan.init(mode=WLAN.AP, ssid='Wipy - Mirobot 2.0', auth=(WLAN.WPA2,'12345678'), channel=7, antenna=WLAN.INT_ANT)
        #wlan.init(mode=WLAN.AP, ssid='Wipy - Mirobot 2.0', auth=(None,''), channel=7, antenna=WLAN.INT_ANT)
        #wlan.init(mode=WLAN.AP, ssid='Wipy - Mirobot 2.0', auth=None, channel=7, antenna=WLAN.INT_ANT)
        #wlan.init(mode=WLAN.AP, ssid='Wipy - Mirobot 2.0 - 00002', auth=None, channel=7, antenna=WLAN.INT_ANT)
        #wlan.init(mode=WLAN.AP, ssid='Wipy - Mirobot 2.0 - 00002', auth=None, channel=7, antenna=WLAN.INT_ANT)
        #wlan.init(mode=WLAN.AP, ssid='Wipy - Mirobot 2.0 - 00004', auth=None, channel=7, antenna=WLAN.INT_ANT)
        wlan.init(mode=WLAN.AP, ssid='Wipy - Mirobot 2.0 - 00005', auth=None, channel=7, antenna=WLAN.INT_ANT)

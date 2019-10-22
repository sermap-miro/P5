
import machine
#from commande import Read_Prgm

#Entrée
#BP = machine.Pin('P17', mode=machine.Pin.IN, pull=None)
# ARRET_URGENCE = machine.Pin('P17', mode=machine.Pin.IN, pull=None)
ARRET_URGENCE = machine.Pin('P17', mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)

#Sortie
#BUZZER = machine.Pin('P21', mode=machine.Pin.OUT)#Version 3.3V
BUZZER = machine.Pin('P19', mode=machine.Pin.OUT)#Version 3.3V
BUZZER(False)

from mirobot2 import m
from time import sleep, time

_en_urgence = False

_nombre_de_seconde_capture = 5

import _thread

def Start_Prgm(numero_programme):
    from commande import Read_Prgm
    print("Démarrage du programme {}".format(numero_programme))
    Resultat_Execution = Read_Prgm(numero_programme) # on lance le programme 1 comme programme par défaut


def Arret_Urgence(arg):
    #_etat_irq = machine.disable_irq()
    global _en_urgence
    global _nombre_de_seconde_capture
    if not _en_urgence:
        _en_urgence = True # pour empecher d'executer en parallèle des cycles de détection de départ
        m.bloque()
        if m.Run_Prgm == 1:
            sleep(1)
            m.bloque()
            m.reset()
        else:
            _tps_depart=time()
            _compteur_impulsion_arret_urgence = 0
            _etat_arret_urgence = ARRET_URGENCE()
            while time()  - _tps_depart < _nombre_de_seconde_capture: # on fait une vérification pendant les 5 prochaines secondes du nombre d'allez-retour
                _ARRET_URGENCE = ARRET_URGENCE()
                if _etat_arret_urgence != _ARRET_URGENCE:
                    _etat_arret_urgence = _ARRET_URGENCE
                    _compteur_impulsion_arret_urgence += 1 # On compte chaque changement d'état (pas le nombre d'enfoncement)
                    sleep(0.2) # protection anti-rebond
            print('Compteur Impulsion = {}'.format(_compteur_impulsion_arret_urgence))
            if _compteur_impulsion_arret_urgence == 1: # au moins trois aller/retour du bouton arrêt urgence
                if not ARRET_URGENCE(): # le bouton arrêt urgence doit etre désactivé avant les 5 secondes pour autorisé le départ
                    _thread.start_new_thread(Start_Prgm, (1,))
            if _compteur_impulsion_arret_urgence >= 2: # au moins trois aller/retour du bouton arrêt urgence
                if not ARRET_URGENCE(): # le bouton arrêt urgence doit etre désactivé avant les 5 secondes pour autorisé le départ
                    _thread.start_new_thread(Start_Prgm, (2,))
        _en_urgence = False
    #machine.enable_irq(_etat_irq)

ARRET_URGENCE.callback(machine.Pin.IRQ_RISING , Arret_Urgence)



#AV_1 = machine.Pin('P9', mode=machine.Pin.OUT)
#BUZZER_INPUT = machine.Pin('P9', mode=machine.Pin.IN, pull=None)
#BUZZER_INPUT = machine.Pin('P8', mode=machine.Pin.IN, pull=None) # pour SPI

#
# from machine import SPI
# #SPI  pins.
# #SPI_CS   = 'P23'
# SPI_MOSI = 'P10'
# SPI_MISO = 'P11'
# SPI_CLK  = 'P9'
#
#
#
# # SPI_LOW  = 0
# # SPI_HIGH = 1
# #
# # spi_cs = Pin(SPI_CS, mode = Pin.OUT)
# # spi_cs.value(SPI_HIGH)
# #spi = SPI(0, mode=SPI.MASTER, polarity=0, phase=0, baudrate=2000000, pins=(SPI_CLK, SPI_MOSI, SPI_MISO))
#
# #spi = SPI(0, mode=SPI.MASTER, polarity=0, phase=0, baudrate=100000, pins=(SPI_CLK, SPI_MOSI, SPI_MISO))
# spi = SPI(0, mode=SPI.MASTER, polarity=0, phase=0, baudrate=57600, pins=(SPI_CLK, SPI_MOSI, SPI_MISO))

# this uses the SPI non-default pins for CLK, MOSI and MISO (``P19``, ``P20`` and ``P21``)
#spi = SPI(0, mode=SPI.MASTER, baudrate=2000000, polarity=0, phase=0, pins=('P19','P20','P21'))

#
# spi.write(bytes([0x56, 0x34, 0x37]))
# spi.write(bytes([0x56, 0x34, 0x34, 0x37]))
# spi.write(bytes([0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39]))
#
#
# #spi.write(bytes([0x53, 0x13])) # "SOmega"
# spi.write(bytes([0x53, 0x0d])) # "S\r"
# spi.write(bytes([0x54])) # "T"
#
# spi.read(4)
#
#
#
#
# spi.write(bytes([0x30]))
# time.sleep(0.1)
# spi.write(bytes([0x31]))
# time.sleep(0.1)
# spi.write(bytes([0x32]))
# time.sleep(0.1)
# spi.write(bytes([0x33]))
# time.sleep(0.1)
# spi.write(bytes([0x34]))
# time.sleep(0.1)
# spi.write(bytes([0x35]))
# time.sleep(0.1)
# spi.write(bytes([0x36]))
# time.sleep(0.1)
# spi.write(bytes([0x37]))
# time.sleep(0.1)
# spi.write(bytes([0x38]))
# time.sleep(0.1)
# spi.write(bytes([0x39]))
# time.sleep(0.1)

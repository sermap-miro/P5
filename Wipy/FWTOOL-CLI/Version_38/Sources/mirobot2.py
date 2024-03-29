# -*- coding: utf-8 -*-
#Version 16: Bug accès web corrigé
#Version 14: Création d'une nouvelle commande: E similaire de DVT, mais pour la marche arrière
#
# Version 9: Gestion Web Modifier (peut mettre l'heure depuis l'interface web)
#
# Version 8: prise en compte de l'affichage des indices de version
#
#
#




from es import ARRET_URGENCE, BUZZER


# import ubinascii
# import socket
import time

import pycom


import machine

from machine import UART, SPI

#from machine import SPI
#SPI  pins.
#SPI_CS   = 'P23'
SPI_MOSI = 'P10'
SPI_MISO = 'P11'
SPI_CLK  = 'P9'



adc= machine.ADC()

#PELLE_TEMPS_s = 10
#PELLE_TEMPS_s = 60


#V_BATTERIE_FAIBLE = 22.3 # Volt
#Conversion_Volt_Lopy = 3.3/4095 # 11 dB
Conversion_Volt_Lopy = 1.1/4095 # 0 dB
#Facteur_Pont_Resistance_30V = 9.3
#Facteur_Pont_Resistance_30V = 9.78
#6 Septembre 2018
#Facteur_Pont_Resistance_30V = 9.93
Facteur_Pont_Resistance_30V = 34

#from config import Facteur_Pont_Resistance_30V

from config import Batt_Mean


Facteur_Conversion_Ampere_2_CAN = 5


_NOIR = 0x000000
_VERT = 0x007F00
_VERT_CLAIR = 0x001000
_BLEU = 0x00007F
_BLEU_CLAIR = 0x000010
#_ROUGE = 0x7F0000
_ROUGE = 0x400000
_ROUGE_CLAIR = 0x100000
_JAUNE = 0x7F7F00
_JAUNE_CLAIR = 0x101000

_TYPE_MOUVEMENT_PION = 0
_TYPE_MOUVEMENT_TEMPS = 1

_AVANT = 1
_ARRIERE = 0
_MONTE = 1
_DESCEND = 0
_SORT = 1
_RENTRE = 0

_LIBRE = 0
_OCCUPER = 1
_ALARME = 2
_PIC_NE_REPOND_PAS = 3
#from machine import Timer
# from mirobot2 import _AVANT, _ARRIERE, _MONTE, _DESCEND, _SORT, _RENTRE, _LIBRE, _OCCUPER, _TYPE_MOUVEMENT_PION, _TYPE_MOUVEMENT_TEMPS
# option_multitas=0




class Mirobot:
    #self.CAPTEUR_PION = machine.Pin('P19', mode=machine.Pin.IN, pull=None)
    #self.CAPTEUR_CAPOT = machine.Pin('P20', mode=machine.Pin.IN, pull=None)


    #def __init__(self, mir_id = 0, arm_id="00000"):
    def __init__(self):
    #def __init__(self, mir_id = 0, arm_id="00000", communication_socket=s):
    #def __init__(self, mir_id = 0, arm_id="00000", communication_socket=communication_socket):
        self.version = 38 # Correction Bug page Planning
        #self.version = 16
        self.nom = 'm'
        self.STATUT_BRUT = ''
        self.STATUT_PIC = ''
        self.Action = ''
        self.busy = _LIBRE
        self.Etat = 'Attente Instruction'
        self.Etat_Pelle = 'Baissé'
        self.Erreur = ''
        self.Run_Prgm = 0
        #self.Prgm_Indice = ''
        self.print_out = 0
        self.verrou = 0
        self.Tag_Cmd = 0 # permettra de stocker si nécessaire, un numéro de commande

        #self.Capteur_Capot_Nb_Evenement_Autoriser = 3
        self.Capteur_Capot_Nb_Evenement_Autoriser = 5 # 13 mai 2019
        #self.Capteur_Capot_Nb_Evenement_Autoriser = 5 # Norvege
        self.Capteur_Capot_Nb_Evenement = 0
        self.Capteur_Capot_Evenement = 0
        self.Capteur_Pion = ''
        self.Capteur_Pion_Nb_Evenement = 0
        self.Capteur_Pion_Evenement = 0
        #self.Nb_Signal_Pion = 0
        self.Marche_Forcer = 0
        self.PION = 0
        self.PLATINE = 0
        self.PION_TEMPS_100ms = 2
        #self.PLATINE_TEMPS_100ms = 30
        #self.PLATINE_TEMPS_100ms = 22 # modif du 18 Juin 2018
        self.PLATINE_TEMPS_100ms = 30 # modif du 19 Juin 2018
        #self.PATINAGE_TEMPS_s = 90
        self.PATINAGE_TEMPS_s = 50 # modif du 17 avril
        self.PATINAGE_NB_ESSAI = 3

        # self.Nb_Seconde_Moteur_1 =
        # self.Nb_Seconde_Moteur_2 =
        self.Nb_Seconde_Pelle = 30
        self.Nb_Seconde_Bequille = 30
        self.Nb_Seconde_Bequille_Mvt = 5

        self.Nb_Seconde_Fonctionnement = 0
        self.Nb_Seconde_Maintenance = 0

        #Valeur du courant moteur
        self.I_Moteur_1 = 0
        self.I_Moteur_2 = 0
        #Consigne moteur
        self.Moteur_Consigne = 20 * 5 # Ampères
        self.Moteur_1_Consigne = 20 * 5  # Ampères
        self.Moteur_2_Consigne = 20 * 5# Ampères
        self.Moteur_X_Consigne = 20 * 5# Ampères
        #self.Moteur_Z_Consigne = 4 # Ampères
        self.Moteur_Z_Consigne = 20 * 5 # Ampères
        #self.Moteur_Z_Seuil = 22 * 5 # Ampères
        self.Moteur_Bequille_Consigne = 20 * 5 # Ampères
        self.Moteur_X_Limite_Courant = 20 * 5 # Ampères
        #self.Moteur_Z_Limite_Courant = 45
        self.Moteur_Z_Limite_Courant = 22 * 5
        self.Moteur_Bequille_Limite_Courant = 22 * 5

        self.V_BATTERIE_FAIBLE = 22.3 # Volt



        self.LED = machine.Pin('P20', mode=machine.Pin.OUT)
        self.LED(True)
        #self.BUZZER = machine.Pin('P21', mode=machine.Pin.OUT)
        self.BUZZER = machine.Pin('P19', mode=machine.Pin.OUT)
        self.BUZZER(False)

        #self.BATTERIE = adc.channel(pin='P13', attn=machine.ADC.ATTN_11DB)
        self.BATTERIE = adc.channel(pin='P13', attn=machine.ADC.ATTN_0DB)
        #0.00815919327063187 * _BATTERIE + 2.61834435852431
        # self.batterie_reg_a = 0.00815919327063187
        # self.batterie_reg_b = 2.61834435852431
        #Valeurs par défaut à ajuster pour coller à la moyenne des cartes électroniques
        self.batterie_10_v = 918.2
        self.batterie_30_v = 3366

        #self.uart_PIC = UART(1, baudrate=115200)
        self.uart_PIC = UART(1, baudrate=9600, pins=('P3','P4'))
        self.spi = SPI(0, mode=SPI.MASTER, polarity=0, phase=0, baudrate=57600, pins=(SPI_CLK, SPI_MOSI, SPI_MISO))
        #self.spi = spi
        #self.uart_PIC = UART(1, baudrate=9600, pins=('P3','P4'))
        #self.uart_PIC.write('\r') #Initialisation du PIC
        self.spi_lock = 0

        self.chrono = machine.Timer.Chrono() # Chrono Embarqué

        self.wifi_name = 'P5'
        self.wifi_nom = ''

        self.Mode_List = { 'MANUEL' : '0',
        'FILO' : '1',
        'PILO' : '2',
        'PAUSE': '3',
        'AU' : '5'
        }

        self.Etat_List = { 0 : 'Inactif',
        1 : 'Alarme',
        2 : 'Avance',
        3 : 'Recule',
        5 : 'Lève la Pelle',
        4 : 'Baisse la Pelle',
        6 : 'Platine',
        7 : 'Bloquer',
        10 : 'Pailleux',
        11 : 'DVT',
        12 : 'Multitas',
        255 : 'Démarrage'
        }



        self.Erreur_List = { '0' : 'NULL',
        '1' : 'RX_LORA',
        '2' : 'Arrêt Urgence',
        '3' : 'Sécu',
        '4' : 'Filo Absent',
        '5' : 'Batterie Faible',
        '6' : 'Dérapage',
        '7' : 'Patinage'}


        self.Etat_PIC_List = { 0 : 'Inactif',
        1 : 'Alarme',
        2 : 'Avance',
        3 : 'Recule',
        5 : 'Lève la Pelle',
        4 : 'Baisse la Pelle',
        6 : 'Platine',
        7 : 'Bloquer',
        8 : 'Rentre la Bequille',
        9 : 'Sort la Bequille',
        10 : 'Pailleux',
        11 : 'DVT',
        12 : 'Multitas',
        70 : 'Bloquer Impossible',
        77 : 'Bloquer Définitivement',
        255 : 'Démarrage'
        }

        self.Etat_Pelle_Intitule = { '0' : 'Baissé',
        '1' : 'Levé'
        }

        self.Erreur_PIC_List = { 0 : 'NULL',
        1 : 'I_Moteur_1',
        2 : 'I_Moteur_2',
        3 : 'Patinage',
        4 : 'Capot',
        5 : 'Overload_Cap_1_2',
        6 : 'Faux Depart',
        7 : 'Arret Urgence',
        8 : 'Batterie Faible',
        9 : 'Overload_Cap_1_1',
        10 : 'Overload_Cap_1_3'}#,
        # '6' : 'Dérapage',
        # '7' : 'Patinage'}

        self.Cause_AU_LIST = { 0 : 'NULL',
        1 : 'Bouton AU',
        2 : 'Mode AU',
        3 : 'MIROBOT CMD AU',
        4 : 'ARMOIRE CMD AU',
        5 : 'Batterie Faible AU'}

        self.FILO_AVAR_LIST = { 0 : 'Av',
        1 : 'Ar'}


# m.PIC_ASK('i')
# m.PIC_ASK('p')
# m.PIC_ASK('s')
# m.PIC_ASK('S')

# m.Consigne(8)
# m.Moteur_Consigne=100
# m.PIC_PARAM_UPDATE()
# m.uart_PIC.write('p\r')#statut moteur
# m.uart_PIC.write('s\r')#statut
# m.uart_PIC.write('e\x00\r') #<= Etat Inactif
# m.uart_PIC.write('e\x06\r') #<= Etat Platine
# m.uart_PIC.readall()
# m.uart_PIC.write('f\x57\r') #nombre de seconde de fonctionnement = 80
# m.uart_PIC.write('I\x00\r'.format(0)) #<= simulation d'un evenement capot
# m.uart_PIC.write('I{}\r'.format(bytes([0]))) #<= simulation d'un evenement capot
# m.uart_PIC.write('I{}\r'.format(0)) #<= simulation d'un evenement capot


    def Consigne(self, consigne=0):
        self.Moteur_Consigne = consigne
        self.PIC_PARAM_UPDATE()

# m.PIC_ASK('E{}'.format(0)) #donne l'état de l'action en cours
# m.PIC_ASK('E{}'.format(1)) #donne l'état de l'action précédente
# m.PIC_ASK('V0')
# m.PIC_ASK('V1')
# m.PIC_ASK('V9')

    def PIC_PARAM_VIEW(self):
        print(self.PIC_ASK('V0'))

    def PARAM_CLEAR(self):
        pycom.nvs_erase_all()

    def PARAM_STORE(self):
        pycom.nvs_set('PAT', int(self.PATINAGE_TEMPS_s))
        pycom.nvs_set('MXC', int(self.Moteur_X_Consigne))
        pycom.nvs_set('MZC', int(self.Moteur_Z_Consigne))
        pycom.nvs_set('MZS', int(self.Moteur_Z_Limite_Courant))
        pycom.nvs_set('MBC', int(self.Moteur_Bequille_Consigne))
        pycom.nvs_set('MBS', int(self.Moteur_Bequille_Limite_Courant))
        pycom.nvs_set('NSP', int(self.Nb_Seconde_Pelle))
        pycom.nvs_set('IT1', int(self.PION_TEMPS_100ms))
        pycom.nvs_set('LT1', int(self.PLATINE_TEMPS_100ms))
        # pycom.nvs_set('BRA', int(self.batterie_reg_a))
        # pycom.nvs_set('BRB', int(self.batterie_reg_b))
        pycom.nvs_set('BV1', int(10 * self.batterie_10_v))
        pycom.nvs_set('BV3', int(10 * self.batterie_30_v))
        pycom.nvs_set('COL', self.Capteur_Capot_Nb_Evenement_Autoriser)



    # def Chrono_Store(self, Fonctionnement=self.Nb_Seconde_Fonctionnement, Maintenance=self.Nb_Seconde_Maintenance):
    #     pycom.nvs_set('TPS', int(Fonctionnement))
    #     pycom.nvs_set('TMA', int(Maintenance))

    def PIC_PARAM_UPDATE(self):
        #self.uart_PIC.write('\r')
        time.sleep(0.1)
        self.PIC_SEND('P0{:03d}'.format(self.Moteur_Consigne))
        time.sleep(0.04)
        self.PIC_SEND('P1{:03d}'.format(int(self.PATINAGE_TEMPS_s)))
        time.sleep(0.04)
        self.PIC_SEND('P2{:03d}'.format(int(self.PION_TEMPS_100ms)))
        time.sleep(0.04)
        self.PIC_SEND('P3{:03d}'.format(int(self.PLATINE_TEMPS_100ms)))
        time.sleep(0.04)
        self.PIC_SEND('P4{:03d}'.format(self.Nb_Seconde_Pelle))
        time.sleep(0.04)
        self.PIC_SEND('P5{:01d}'.format(self.Capteur_Capot_Nb_Evenement_Autoriser))
        time.sleep(0.04)
        self.PIC_SEND('P6{:01d}'.format(self.PATINAGE_NB_ESSAI))
        time.sleep(0.04)
        self.PIC_SEND('P7{:03d}'.format(self.Moteur_X_Consigne))
        time.sleep(0.04)
        self.PIC_SEND('P8{:03d}'.format(self.Moteur_Z_Consigne))
        time.sleep(0.04)
        self.PIC_SEND('P9{:03d}'.format(self.Moteur_Bequille_Consigne))
        time.sleep(0.04)
        self.PIC_SEND('m1{:03d}'.format(self.Moteur_X_Limite_Courant))
        time.sleep(0.04)
        self.PIC_SEND('m2{:03d}'.format(self.Moteur_Z_Limite_Courant))
        time.sleep(0.04)
        self.PIC_SEND('m3{:03d}'.format(self.Moteur_Bequille_Limite_Courant))


    def PIC_ASK(self, Question=''):
        #self.uart_PIC.write('\r')
        time.sleep(0.1)
        if Question != '':
            # Reponse = self.uart_PIC.readall()
            # self.PIC_SEND(Question)
            # #self.uart_PIC.write(Question + '\r')
            # #time.sleep(0.04)
            # time.sleep(0.48)
            # Reponse = self.uart_PIC.readall()
            #self.PIC_SEND('\r')
            while self.spi_lock == 1:
                time.sleep(0.01)
                pass
            self.spi_lock = 1
            for _ in range(10):
                try:
                    # ... do stuff ...
                    Reponse = self.spi.read(64)
                    self.PIC_SEND(Question)
                    time.sleep(0.48)
                    Reponse = self.spi.read(64)
                    Reponse = Reponse.decode('utf8')
                    Reponse = Reponse.split('\r')[0]
                    if len(Reponse)==0 or Reponse[0]=='U':
                        raise MonException("Erreur de reception")
                except:# SomeTransientError:
                    # ... log it, sleep, etc. ...
                    time.sleep(0.25)
                    continue
                else:
                    break
            else:
                #raise PermanentError()
                pass
            # time.sleep(0.08)
            # Reponse = ''
            # #while len(Reponse)==0 or Reponse[0]
            # Reponse = self.spi.read(64)
            # self.PIC_SEND(Question)
            # time.sleep(0.48)
            # Reponse = self.spi.read(64)
            # Reponse = Reponse.decode('utf8')
            # Reponse = Reponse.split('\r')[0]
            self.spi_lock = 0
            self.affiche('Get from pic <= {}'.format(Reponse))
            return Reponse
            # try:
            #     if len(Reponse)>10:
            #         if Reponse[8] == 13:
            #             Reponse = Reponse[9:] + Reponse[0:8]
            #     self.affiche('Get from pic <= {}'.format(Reponse))
            #     return Reponse
            # except:
            #     return Reponse

    def PIC_SEND(self, Commande=''):
        # self.uart_PIC.write('\r')
        # time.sleep(0.01)
        # self.uart_PIC.write('a\r')
        # time.sleep(0.05)
        # self.uart_PIC.write('U')
        # #self.uart_PIC.write('U')
        # time.sleep(0.01)
        if Commande != '':
            self.affiche('Send to pic => {}'.format(Commande))
            #self.uart_PIC.write('\r')
            self.spi.write(bytes([0x0d]))
            time.sleep(0.01)
            #self.uart_PIC.write(Commande + '\r')
            self.spi.write(str.encode(Commande + '\r'))



# m.PIC_LED(0)
# m.PIC_LED(1)
    def PIC_LED(self, Etat=1):
        #self.uart_PIC.write('\r')
        if Etat == 1:
            self.PIC_SEND('L1')
        else:
            self.PIC_SEND('L0')


    def LED_set(self, Couleur=0x000000):
        pycom.rgbled(Couleur)

    def bip(self, temps_s=1):
        self.BUZZER(True)
        time.sleep(temps_s)
        self.BUZZER(False)

    def affiche(self, Texte=''):
        if self.print_out == 1:
            print('{}'.format(Texte))

    def check_batterie(self):
        _batterie_reg_a = (30 - 10) / (self.batterie_30_v - self.batterie_10_v)
        _batterie_reg_b = (self.batterie_30_v * 10 - self.batterie_10_v * 30) / (self.batterie_30_v - self.batterie_10_v)
        # _BATTERIE = self.BATTERIE()
        # _BATTERIE *= Conversion_Volt_Lopy # Conversion_Volt_Lopy = 3.3/4095
        # #_BATTERIE *= Facteur_Pont_Resistance_30V
        # #_BATTERIE = _BATTERIE * (12.41 - _BATTERIE * 1.05)
        # #_BATTERIE = _BATTERIE * (0.399 * _BATTERIE ** 3 - 3.591 * _BATTERIE ** 2 + 9.389 * _BATTERIE + 2.596)
        # #_BATTERIE = _BATTERIE * (0.433 * _BATTERIE ** 3 - 3.881 * _BATTERIE ** 2 + 10.274 * _BATTERIE + 1.589)
        # #_BATTERIE = _BATTERIE * (-0.495235729505111 * _BATTERIE + 11.9765986103554) #1.2 kOhm 39 kOhm
        # #_BATTERIE = _BATTERIE * (-5.94470199067496 * _BATTERIE + 41.481516771378) #1 kOhm 33 kOhm # 00019
        # #_BATTERIE = _BATTERIE * (-4.93137569470239 * _BATTERIE + 37.3366197430231) #1 kOhm 33 kOhm # 00016
        # #_BATTERIE = _BATTERIE * (-4.96751151733445 * _BATTERIE + 37.457621966586) #1 kOhm 33 kOhm # 00016 # Valeurs extrêmes
        # _BATTERIE = _BATTERIE * (-5.38504199957544 * _BATTERIE + 38.1257032967047) #1 kOhm 33 kOhm # 00013 # Valeurs extrêmes
        # #_BATTERIE = _BATTERIE * (-11.8070198044948 * _BATTERIE + 43.9284242369887) #1 kOhm 33 kOhm # 00013 # Valeurs extrêmes +/- 10 30
        #_BATTERIE = self.BATTERIE()
        _BATTERIE = Batt_Mean(self)
        _BATTERIE = _batterie_reg_a * _BATTERIE + _batterie_reg_b #1 kOhm 33 kOhm # 00013 # Valeurs extrêmes
        if _BATTERIE <= self.V_BATTERIE_FAIBLE:
            self.PIC_ASK('T') # Tension Batterie Defaillante
            time.sleep(0.1)
        #return('{:05.02f}'.format(_BATTERIE))

    def batterie(self):
        try:
            _batterie_reg_a = (30 - 10) / (self.batterie_30_v - self.batterie_10_v)
            _batterie_reg_b = (self.batterie_30_v * 10 - self.batterie_10_v * 30) / (self.batterie_30_v - self.batterie_10_v)
            # _BATTERIE = self.BATTERIE()
            # _BATTERIE *= Conversion_Volt_Lopy
            # #_BATTERIE *= Facteur_Pont_Resistance_30V
            # #_BATTERIE = _BATTERIE * (12.41 - _BATTERIE * 1.05)
            # #_BATTERIE = _BATTERIE * (0.399 * _BATTERIE ** 3 - 3.591 * _BATTERIE ** 2 + 9.389 * _BATTERIE + 2.596)
            # #_BATTERIE = _BATTERIE * (0.433 * _BATTERIE ** 3 - 3.881 * _BATTERIE ** 2 + 10.274 * _BATTERIE + 1.589)
            # #_BATTERIE = _BATTERIE * (-0.495235729505111 * _BATTERIE + 11.9765986103554) #1.2 kOhm 39 kOhm
            # #_BATTERIE = _BATTERIE * (-5.94470199067496 * _BATTERIE + 41.481516771378) #1 kOhm 33 kOhm # 00019
            # #_BATTERIE = _BATTERIE * (-4.93137569470239 * _BATTERIE + 37.3366197430231) #1 kOhm 33 kOhm # 00016
            # #_BATTERIE = _BATTERIE * (-4.96751151733445 * _BATTERIE + 37.457621966586) #1 kOhm 33 kOhm # 00016 # Valeurs extrêmes
            # _BATTERIE = _BATTERIE * (-5.38504199957544 * _BATTERIE + 38.1257032967047) #1 kOhm 33 kOhm # 00013 # Valeurs extrêmes
            # #_BATTERIE = _BATTERIE * (-11.8070198044948 * _BATTERIE + 43.9284242369887) #1 kOhm 33 kOhm # 00013 # Valeurs extrêmes +/- 10 30
            #_BATTERIE = self.BATTERIE()
            _BATTERIE = Batt_Mean(self)
            _BATTERIE = _batterie_reg_a * _BATTERIE + _batterie_reg_b #1 kOhm 33 kOhm # 00013 # Valeurs extrêmes
        except: # est déjà arrivé lorsque les résistances du pont diviseur était incorrect, alors on a eu une division par zéro car self.batterie_30_v = self.batterie_10_v = 4095 (en saturation)
            _BATTERIE = 0
        return('{:05.02f}'.format(_BATTERIE))
        #
        # V_BATTERIE_FAIBLE = 22.3 # Volt
        # Conversion_Volt_Lopy = 3.3/4095
        # Facteur_Pont_Resistance_30V = 9.3

    def get_statut_PIC(self):
        for _ in range(10):
            try:
                # ... do stuff ...
                #self.STATUT_PIC = self.PIC_ASK('s')[:-1]
                #26 Septembre 2018 => depuis le passage en spi il n'y a pas de caractère de fin de chaine!
                self.STATUT_PIC = self.PIC_ASK('s')
                self.Etat = self.Etat_PIC_List[int(self.STATUT_PIC[0:2],16)]
                self.Erreur = self.Erreur_PIC_List[int(self.STATUT_PIC[4:6],16)]
                self.STATUT_PIC = 'Etat={} (previous={}), Erreur={}'.format(self.Etat_PIC_List[int(self.STATUT_PIC[0:2],16)], self.Etat_PIC_List[int(self.STATUT_PIC[2:4],16)], self.Erreur_PIC_List[int(self.STATUT_PIC[4:6],16)])
                print(self.STATUT_PIC)
                self.affiche('STATUT_PIC = {}'.format(self.STATUT_PIC))
            except:# SomeTransientError:
                # ... log it, sleep, etc. ...
                time.sleep(0.25)
                self.affiche('STATUT_PIC EXCEPTION')
                continue
            else:
                break
        else:
            #raise PermanentError()
            self.affiche('get_STATUT_PIC Impossible à récupérer'.format(self.STATUT_PIC))
            pass

        #
        # self.STATUT_PIC = self.PIC_ASK('s')[:-1]
        # self.Etat = self.Etat_PIC_List[int(self.STATUT_PIC[0:2],16)]
        # self.Erreur = self.Erreur_PIC_List[int(self.STATUT_PIC[4:6],16)]
        # self.STATUT_PIC = 'Etat={} (previous={}), Erreur={}'.format(self.Etat_PIC_List[int(self.STATUT_PIC[0:2],16)], self.Etat_PIC_List[int(self.STATUT_PIC[2:4],16)], self.Erreur_PIC_List[int(self.STATUT_PIC[4:6],16)])
        # print(self.STATUT_PIC)


    def get_etat(self,Etat):
        return self.Etat_PIC_List[Etat]
        #return self.Etat_List[Etat]


    def get_erreur(self,Erreur):
        return self.Erreur_PIC_List[Erreur]
        #return self.Erreur_List[Erreur]

    def get_cause_au(self,Cause):
        return self.Cause_AU_LIST[Cause]

#
# { 0 : 'Inactif',
# 1 : 'Alarme',
# 2 : 'Avance',
# 3 : 'Recule',
# 4 : 'Lève la Pelle',
# 5 : 'Baisse la Pelle',
# 255 : 'Démarrage'
# }
    def refresh_statut(self):
        try:
            #Il arrive que le PIC ne réponde pas directement, une seconde interrogation permet en général de s'affranchir de ce problème
            try:
                self.Etat = self.get_etat(int(self.PIC_ASK('E{}'.format(0))))
            except:
                time.sleep(0.5)
                self.Etat = self.get_etat(int(self.PIC_ASK('E{}'.format(0))))
        except:
            pass

    def check_busy(self):
        '''renvoi 1 s'il est libre, 0 en cours de fonctionnement, 2 en alerte'''

        self.check_batterie()
        for _ in range(10):
            try:
                # ... do stuff ...
                self.busy = int(self.PIC_ASK('b'))
                return self.busy
            except SomeTransientError:
                # ... log it, sleep, etc. ...
                self.affiche('PIC busy: essai {}'.format(_))
                time.sleep(0.5)
                continue
            else:
                break
        else:
            pass
            return 3 # le PIC ne répond pas
            #raise PermanentError()


        # _nb_essai = 3
        # #print("Vérification de l'état du Mirobot...")
        # self.check_batterie()
        # try:
        #     #Il arrive que le PIC ne réponde pas directement, une seconde interrogation permet en général de s'affranchir de ce problème
        #     try:
        #         #self.affiche('Check Busy from PIC unresponsive 1st try')
        #         self.busy = int(self.PIC_ASK('b'))
        #     except:
        #         self.affiche('Check Busy from PIC unresponsive 2nd try')
        #         time.sleep(0.5)
        #         try:
        #             self.busy = int(self.PIC_ASK('b'))
        #         except:
        #             self.affiche('Check Busy from PIC unresponsive 3rd try')
        #             time.sleep(0.5)
        #             self.busy = int(self.PIC_ASK('b'))
        #     return self.busy
        #     # if self.Etat in {'Alarme', 'Bloquer'}:
        #     #     print("Mirobot en alerte: " + self.Etat)
        #     #     self.LED_set(_ROUGE)
        #     #     return 2
        #     # if self.Etat == 'Inactif' or self.Etat == 'Platine':
        #     #     print("Mirobot Libre")
        #     #     self.Infinie = 0 # pas vraiment nécessaire, surtout en sécurité, mais si bien fait on ne devrait jamais avoir a resetté cette variable
        #     #     self.LED_set(_VERT_CLAIR)
        #     #     return 1
        #     # else:
        #     #     print("Mirobot non Libre, état = " + self.Etat)
        #     #     #self.LED_set(_JAUNE_CLAIR)
        #     #     self.LED_set(_BLEU_CLAIR)
        #     #     return 0
        # except:
        #     self.affiche('Check Busy from PIC unresponsive')
        #     return 3 # _PIC_NE_REPOND_PAS





# 70 : 'Bloquer Impossible',
# 77 : 'Bloquer Définitivement',
# m.uart_PIC.write('e\x06\r') #<= Etat Platine
    def libre(self):
        '''renvoi 1 s'il est libre, 0 en cours de fonctionnement, 2 en alerte'''
        print("Vérification de l'état du Mirobot...")
        try:
            #Il arrive que le PIC ne réponde pas directement, une seconde interrogation permet en général de s'affranchir de ce problème
            try:
                self.Etat = self.get_etat(int(self.PIC_ASK('E{}'.format(0))))
            except:
                time.sleep(0.5)
                self.Etat = self.get_etat(int(self.PIC_ASK('E{}'.format(0))))
            if self.Etat in {'Alarme', 'Bloquer'}:
                print("Mirobot en alerte: " + self.Etat)
                #self.LED_set(_ROUGE)
                return 2 # _ALARME
            if self.Etat == 'Inactif' or self.Etat == 'Platine':
                print("Mirobot Libre")
                self.Infinie = 0 # pas vraiment nécessaire, surtout en sécurité, mais si bien fait on ne devrait jamais avoir a resetté cette variable
                #self.LED_set(_VERT_CLAIR)
                return 1
            else:
                print("Mirobot non Libre, état = " + self.Etat)
                #self.LED_set(_JAUNE_CLAIR)
                #self.LED_set(_BLEU_CLAIR)
                return 0
        except:
            return 3

    def Somme_de_Controle(self,String):
        return self.Somme_de_Controle_Mirobot(String[0],String[1],String[2],String[3],String[4],String[5],String[6],String[7],String[8],String[9])

    def Somme_de_Controle_Mirobot(self,A,B,C,D,E,F,G,H,I,J):
        CS = 0
        CS ^= ord(A)
        CS ^= ord(B)
        CS ^= ord(C)
        CS ^= ord(D)
        CS ^= ord(E)
        CS ^= ord(F)
        CS ^= ord(G)
        CS ^= ord(H)
        CS ^= ord(I)
        CS ^= ord(J)
        #CS ^= ord('U')
        return CS


    def stat_reset(self):
        self.Capteur_Capot_Nb_Evenement = 0
        self.Capteur_Capot_Evenement = 0
        self.Capteur_Pion_Nb_Evenement = 0
        self.Capteur_Pion_Evenement = 0
        self.PION = 0

    def X(self, direction=0, type_consigne=0, option=0, option_multitas=0, option_pailleux=0):
        """
            Execute le déplacement du module P4 le long de l'axe X (avance ou recule)
        """
        #self.uart_PIC.write('\r')
        time.sleep(0.1)
        if ARRET_URGENCE() == 1: # il y a un probleme
            for _ in range(5):
                self.bip(0.1)
                time.sleep(0.1)
        else:
            #self.reset()
            if option_multitas == 1:
                self.PIC_SEND('X{}{}{:03d}1'.format(direction, type_consigne, option))#self.Moteur_Consigne))
            elif option_pailleux == 1:
                self.PIC_SEND('X{}{}{:03d}2'.format(direction, type_consigne, option))#self.Moteur_Consigne))
            else:
                self.PIC_SEND('X{}{}{:03d}'.format(direction, type_consigne, option))#self.Moteur_Consigne))


    def Z(self, direction=0, type_consigne=0, option=0):
        """
            Execute le déplacement du module P4 le long de l'axe X (avance ou recule)
        """
        #self.uart_PIC.write('\r')
        time.sleep(0.1)
        if ARRET_URGENCE() == 1: # il y a un probleme
            for _ in range(5):
                self.bip(0.1)
                time.sleep(0.1)
        else:
            #self.reset()
            self.PIC_SEND('Z{}{}{:03d}'.format(direction, type_consigne, option))#self.Moteur_Consigne))

    def Bequille(self, direction=0, type_consigne=0, option=0):
        """
            Execute le déplacement du module P4 le long de l'axe X (avance ou recule)
        """
        #self.uart_PIC.write('\r')
        time.sleep(0.1)
        if ARRET_URGENCE() == 1: # il y a un probleme
            for _ in range(5):
                self.bip(0.1)
                time.sleep(0.1)
        else:
            #self.reset()
            self.PIC_SEND('B{}{}{:03d}'.format(direction, type_consigne, option))#self.Moteur_Consigne))


    def avance(self, Reset=1, Nb_Pion=0, Nb_Seconde=0, option_triple=0, option_multitas=0):
        self.PION = 0
        #self.Etat = self.Etat_List['8'] # 'Avance'
        #self.Etat = self.Etat_List[2] # 'Avance'
        self.Etat = self.Etat_PIC_List[2] # 'Avance'
        #self.Action = ''
        if Reset == 1:
            self.stat_reset()
        if Nb_Pion==0 and  Nb_Seconde==0:
            #self.X(direction=_AVANT, type_consigne=_TYPE_MOUVEMENT_PION, option=0)
            #self.X(direction=_AVANT, type_consigne=_TYPE_MOUVEMENT_PION, option=option_multitas)
            self.X(direction=_AVANT, type_consigne=_TYPE_MOUVEMENT_PION, option=0, option_multitas=option_multitas)
            return
        if Nb_Pion!=0:
            self.X(direction=_AVANT, type_consigne=_TYPE_MOUVEMENT_PION, option=Nb_Pion)
        else:
            #Nb_Seconde
            Nb_Seconde *= 16 #permet d'ignorer le décalage à droite dans les options de la fonction Mouvement_X du PIC
            if option_triple==1:
                Nb_Seconde += 4
            self.X(direction=_AVANT, type_consigne=_TYPE_MOUVEMENT_TEMPS, option=Nb_Seconde)
        #self.PIC_SEND('X11{:03d}'.format(self.Moteur_Consigne))
        #m.PIC_SEND('M11{:03d}'.format(m.Moteur_Consigne))
        #print("Mirobot avance()")

    def recule(self, Reset=1, Nb_Pion=0, Nb_Seconde=0, option_triple=0, option_pailleux=0):
        self.PION = 0
        #self.Etat = self.Etat_List['9'] # 'Recule'
        #self.Etat = self.Etat_List[3] # 'Recule'
        self.Etat = self.Etat_PIC_List[3] # 'Recule'
        if Reset == 1:
            self.stat_reset()
        #self.X(direction=_ARRIERE, type_consigne=_TYPE_MOUVEMENT_PION, option=0)
        if Nb_Pion==0 and  Nb_Seconde==0:
            self.X(direction=_ARRIERE, type_consigne=_TYPE_MOUVEMENT_PION, option=0)
            return
        if Nb_Pion!=0:
            self.X(direction=_ARRIERE, type_consigne=_TYPE_MOUVEMENT_PION, option=Nb_Pion)
        else:
            Nb_Seconde *= 16 #permet d'ignorer le décalage à droite dans les options de la fonction Mouvement_X du PIC
            if option_triple==1:
                Nb_Seconde += 4
            self.X(direction=_ARRIERE, type_consigne=_TYPE_MOUVEMENT_TEMPS, option=Nb_Seconde, option_pailleux=option_pailleux)

    def baisse_la_pelle(self):
        #self.Etat = self.Etat_List[4] # 'Baisse la Pelle'
        self.Etat = self.Etat_PIC_List[4] # 'Baisse la Pelle'
        print("Mirobot baisse la pelle()")
        self.Z(direction=_DESCEND, type_consigne=_TYPE_MOUVEMENT_TEMPS, option=self.Nb_Seconde_Pelle)

    def leve_la_pelle(self):
        #self.Etat = self.Etat_List[5] #'Lève la Pelle'
        self.Etat = self.Etat_PIC_List[5] #'Lève la Pelle'
        print("Mirobot leve la pelle()")
        self.Z(direction=_MONTE, type_consigne=_TYPE_MOUVEMENT_TEMPS, option=self.Nb_Seconde_Pelle)

    def sort_la_bequille(self):
        #self.Etat = self.Etat_List[9] # 'Sort la Béquille'
        self.Etat = self.Etat_PIC_List[9] # 'Sort la Béquille'
        print("Mirobot sort la béquille()")
        self.Bequille(direction=_SORT, type_consigne=_TYPE_MOUVEMENT_TEMPS, option=self.Nb_Seconde_Bequille)

    def rentre_la_bequille(self):
        #self.Etat = self.Etat_List[5] # 'Rentre la Béquille'
        self.Etat = self.Etat_PIC_List[5] # 'Rentre la Béquille'
        print("Mirobot rentre la béquille()")
        self.Bequille(direction=_RENTRE, type_consigne=_TYPE_MOUVEMENT_TEMPS, option=self.Nb_Seconde_Bequille)




    def bequille(self, Direction=1):
        if Direction == 1:
            self.sort_la_bequille()
        else:
            self.rentre_la_bequille()

    def pelle(self, Direction=1):
        if Direction == 1:
            self.leve_la_pelle()
        else:
            self.baisse_la_pelle()

    def allumer(self, Broche):
        Broche(False) # Entré inversé
        #Broche(True)

    def eteindre(self, Broche):
        Broche(True) # Entré inversé
        #Broche(False)

    def etat(self, Broche):
        return Broche.value() == 1

    def start(self):
        print("Mirobot start")

    def coupe_moteur(self):
        #self.uart_PIC.write('\r')
        time.sleep(0.1)
        self.PIC_SEND('e\x00')



    def reset(self):
        #self.uart_PIC.write('\r')
        time.sleep(0.1)
        self.PIC_SEND('r')
        #self.PIC_SEND('e\x07')#Etat Bloquer

    def bloque(self):
        #self.uart_PIC.write('\r')
        time.sleep(0.1)
        if self.Run_Prgm == 1:
            self.Run_Prgm = 0
        self.PIC_SEND('H')
        #self.PIC_SEND('e\x07')#Etat Bloquer

    def au(self):
        #self.uart_PIC.write('\r')
        time.sleep(0.1)
        #self.PIC_SEND('U')
        self.PIC_SEND('W')
        #self.coupe_moteur()
        #time.sleep(0.4)

    def alarme(self):
        #self.uart_PIC.write('\r')
        time.sleep(0.1)
        m.PIC_SEND('e\x4D') # Etat bloquer definitivement
        time.sleep(0.1)
        self.get_statut_PIC()
        while self.Etat == 'Bloquer Définitivement':
            for _ in range(5):
                self.bip(0.1)
                time.sleep(0.1)
            time.sleep(30)
            self.get_statut_PIC()

    def stop(self, cause=None):
        #self.PIC_SEND('e\x00')
        self.coupe_moteur()
        if cause == None:
            print('mirobot stop()')
        else:
            print('mirobot stop('+ cause +')')
        #self.patinage_detection.stop()
        #self.Etat = self.Etat_List[0] if cause is None else cause # 'Attente Instruction'
        #self.commande_TAG(Commande='C0013')


m=Mirobot()
